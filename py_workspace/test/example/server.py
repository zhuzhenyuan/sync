# coding:utf8
import os
import random
import json
import time
import tornado.ioloop
import tornado.web

db = {}  # 全局数据，保存游戏数据
db_path = './data.db'  # 数据库文件


# 数据读取初始化
def db_read():
    global db
    if os.path.exists(db_path):
        with open(db_path, 'r') as f:
            db = json.loads(f.read())

# 保存数据到文件
def db_write():
    global db
    tmp = {}
    if os.path.exists(db_path):
        with open(db_path, 'r') as f:
            tmp = json.loads(f.read())
    with open(db_path, 'w') as f:
        tmp.update(db)
        f.write(json.dumps(tmp))


# 数据处理类
class DataHandle(object):
    @classmethod
    def init(cls):
        db_read()
        print('init db')

    @classmethod
    def exit_game(cls):
        if db:
            db_write()
        # exit(0)

    @classmethod
    def handler_game_login(cls, choose, username, passwd):
        choose = int(choose)
        if choose == 2:  # 注册
            if username in db:
                return False
            db[username] = {
                'passwd': passwd
            }
            db_write()
        elif choose == 1:  # 登录
            if username not in db or passwd != db[username]['passwd']:
                return False
        else:
            return False
        return True

    @classmethod
    def game_random_num(cls, username, difficulty):
        difficulty = int(difficulty)
        db[username]['difficulty'] = difficulty  # 保存难度
        # 随机数字
        if difficulty == 1:
            db[username]['num'] = random.randint(1, 100)
        elif difficulty == 2:
            db[username]['num'] = random.randint(1, 1000)
        elif difficulty == 3:
            db[username]['num'] = random.randint(1, 10000)
        db[username]['start_time'] = time.time()  # 记录开始时间
        return db[username]['num']
    
    @classmethod
    def game_check_num(cls, username, num):
        num = int(num)
        user_data = db[username]
        if user_data['num'] == num:
            difficulty = user_data['difficulty']

            user_data['end_time'] = time.time()  # 记录结束时间
            time_cost = user_data['end_time'] - user_data['start_time']  # 计算当前游戏完成时间
            user_data.setdefault('play_time', []).append(time_cost)  # 放入历史
            user_data['points'] = user_data.get('points', 0) + 10 * difficulty  # 计算保存积分
            user_data['frequency'] = user_data.get('frequency', 0) + 1  # 记录玩的次数+1

            # 记录每个难度最短的完成时间
            if 'time_cost' not in user_data or difficulty not in user_data['time_cost']:
                user_data.setdefault('time_cost', {})[difficulty] = time_cost
            else:
                user_data['time_cost'][difficulty] = min(user_data['time_cost'][difficulty], time_cost)
            return 0
        elif user_data['num'] > num:
            return -1
        else:
            return 1

    @classmethod
    def game_get_info(cls, username):
        t = db[username]['end_time'] - db[username]['start_time']  # 获取当前局完成时间
        t_average = sum(db[username]['play_time']) / len(db[username]['play_time'])  # 获取所有的平均游玩时间
        return t, t_average, db[username]['points']

    @classmethod
    def game_get_points_leaderboard(cls):
        l = []
        for k, v in db.items():
            if 'points' not in v:
                continue
            l.append((k, v['points']))
        
        l = sorted(l, key=lambda d: d[1], reverse=True)
        return l[:10]  # 获取积分排行
    
    @classmethod
    def game_get_frequency_leaderboard(cls):
        l = []
        for k, v in db.items():
            if 'frequency' not in v:
                continue
            l.append((k, v['frequency']))
        
        l = sorted(l, key=lambda d: d[1], reverse=True)
        return l[:10]  # 获取玩的次数排行


class GameLogin(tornado.web.RequestHandler):
    def get(self):  # get请求的一种方式(另外常见还有post)
        args = self.get_arguments('args')  # 获取传入的参数
        # choose, username, passwd = args
        # ret = DataHandle.handler_game_login(choose, username, passwd)
        ret = DataHandle.handler_game_login(*args)
        self.write({'args': ret})


class GameExit(tornado.web.RequestHandler):
    def get(self):
        DataHandle.exit_game()


class GameRandomNum(tornado.web.RequestHandler):
    def get(self):
        args = self.get_arguments('args')
        ret = DataHandle.game_random_num(*args)
        self.write({'args': ret})


class GameCheckNum(tornado.web.RequestHandler):
    def get(self):
        args = self.get_arguments('args')
        ret = DataHandle.game_check_num(*args)
        self.write({'args': ret})

class GameGetInfo(tornado.web.RequestHandler):
    def get(self):
        args = self.get_arguments('args')
        ret = DataHandle.game_get_info(*args)
        self.write({'args': ret})


class GameGetPointsLeaderboard(tornado.web.RequestHandler):
    def get(self):
        ret = DataHandle.game_get_points_leaderboard()
        self.write({'args': ret})


class GameGetFrequencyLeaderboard(tornado.web.RequestHandler):
    def get(self):
        ret = DataHandle.game_get_frequency_leaderboard()
        self.write({'args': ret})


def make_app():
    return tornado.web.Application([
        (r"/game/login", GameLogin),  # url及处理方法，，前部分网络地址表示指定得请求，后面是该请求执行的代码
        (r"/game/exit", GameExit),
        (r"/game/random", GameRandomNum),
        (r"/game/check", GameCheckNum),
        (r"/game/info", GameGetInfo),
        (r"/game/leaderboard/points", GameGetPointsLeaderboard),
        (r"/game/leaderboard/frequency", GameGetFrequencyLeaderboard),
	])


def run():
    DataHandle.init()
    app = make_app()
    app.listen(9999)  # 监听端口 8888，网络服务提供服务都有一个端口号
    tornado.ioloop.IOLoop.current().start()  # 启动服务

if __name__ == "__main__":
    run()
