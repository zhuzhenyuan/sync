# coding:utf8
import os
import random
import json
import time

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


def get_input_option():
    while True:
        try:
            return int(input())
        except:
            print("please input again")


def get_input_str():
    return input().strip()



class PromptText(object):
    TextWelcome = '''
    *********************************************
    ***   welcome come to game                ***
    ***   please choose an option             ***
    *********************************************
    '''

    TextLoginOption = '''
    menu
    1: login
    2: register
    3: exit game
    '''
    # 可以再加个 Logout
    TextStartGame = '''
    menu
    1: start game
    2: 积分排行榜
    3: 玩的次数排行榜
    4: exit game
    '''
    TextChooseDifficulty = '''
    difficulty choice
    1: 1-100
    2: 1-1000
    3: 1-10000
    '''


# 页面处理类
class Pages(object):
    @classmethod
    def login_page(cls):
        print("login now")
        print("please input username")
        username = get_input_str()
        print("please input password")
        passwd = get_input_str()
        return username, passwd

    @classmethod
    def register_page(cls):
        print("register now")
        print("please input username")
        username = get_input_str()
        print("please input password")
        passwd = get_input_str()

        return username, passwd

    @classmethod
    def exit_game(cls):
        if db:
            db_write()
        exit(0)


# 数据处理类
class DataHandle(object):
    @classmethod
    def handler_game_login(cls, choose, username, passwd):
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
        db[username]['difficulty'] = difficulty  # 保存难度
        # 随机数字
        if difficulty == 1:
            db[username]['num'] = random.randint(1, 100)
        elif difficulty == 2:
            db[username]['num'] = random.randint(1, 1000)
        elif difficulty == 2:
            db[username]['num'] = random.randint(1, 10000)
        db[username]['start_time'] = time.time()  # 记录开始时间
        return db[username]['num']
    
    @classmethod
    def game_check_num(cls, username, num):
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


class Game(object):
    @classmethod
    def init(cls):
        db_read()

    @classmethod
    def game_login(cls):
        op_pages = {
            1: Pages.login_page,
            2: Pages.register_page,
            3: Pages.exit_game,
        }
        print(PromptText.TextWelcome)
        while True:
            print(PromptText.TextLoginOption)
            choose = get_input_option()
            if choose not in op_pages:
                print("please choose an option")
                continue

            ret = op_pages[choose]()
            if ret:
                username, passwd = ret
                status = DataHandle.handler_game_login(choose, username, passwd)
                if status:
                    if choose == 2:
                        print("register success, please login")
                    elif choose == 1:
                        print("login success, enjoy it")
                        return username
                else:
                    if choose == 2:
                        print("user already exists")
                    elif choose == 1:
                        print("username or password error, please login again")

    @classmethod
    def start(cls, username):
        op_pages = {
            1: cls.start_game,
            2: DataHandle.game_get_points_leaderboard,
            3: DataHandle.game_get_frequency_leaderboard,
            4: Pages.exit_game,
        }
        while True:
            print(PromptText.TextStartGame)
            choose = get_input_option()
            if choose not in op_pages:
                print("please choose an option")
                continue
            if choose in (2, 3, 4):
               data = op_pages[choose]()
               if data:
                   for d in data:
                       print(d)
            else:
                op_pages[choose](username)

    @classmethod
    def start_game(cls, username):
        print(PromptText.TextChooseDifficulty)
        choose = 0
        while True:
            choose = get_input_option()
            if choose not in (1, 2, 3):
                print('please choose again')
                continue
            break
        DataHandle.game_random_num(username, choose)
        print('请猜')
        while True:
            num = get_input_option()
            status = DataHandle.game_check_num(username, num)
            if status == 0:
                t, t_average, points = DataHandle.game_get_info(username)
                print("猜中了, 用时%d s, 平均用时 %d s, 当前积分 %d" % (t, t_average, points))
                break
            elif status == -1:
                print("猜小了")
            else:
                print("猜大了")


def run():
    Game.init()
    username = Game.game_login()
    if username:
        print("login success")
    Game.start(username)


if __name__ == "__main__":
    run()
