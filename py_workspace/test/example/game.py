import os
import random
import json

db = {}
db_path = './data.db'


def db_read():
    global db
    if os.path.exists(db_path):
        with open(db_path, 'r') as f:
            db = json.loads(f.read())


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
    1: login
    2: register
    3: exit game
    '''
    TextStartGame = '''
    1: start game
    2: exit game
    '''
    TextChooseDifficulty = '''
    1: 1-100
    2: 1-1000
    3: 1-10000
    '''



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


class DataHandle(object):
    Num = 0
    @classmethod
    def handler_game_login(cls, choose, username, passwd):
        if choose == 2:
            if username in db:
                return False
            db[username] = {
                'passwd': passwd
            }
        elif choose == 1:
            if username not in db or passwd != db[username]['passwd']:
                return False
        else:
            return False
        return True

    @classmethod
    def game_random_num(cls, difficulty):
        if difficulty == 1:
            cls.Num = random.randint(1, 100)
        elif difficulty == 2:
            cls.Num = random.randint(1, 1000)
        elif difficulty == 2:
            cls.Num = random.randint(1, 10000)
        return cls.Num


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
                        return True
                else:
                    if choose == 2:
                        print("user already exists")
                    elif choose == 1:
                        print("username or password error, please login again")

    @classmethod
    def start(cls):
        op_pages = {
            1: cls.start_game,
            2: Pages.exit_game,
        }
        while True:
            print(PromptText.TextStartGame)
            choose = get_input_option()
            if choose not in op_pages:
                print("please choose an option")
                continue
            op_pages[choose]()

    @classmethod
    def start_game(cls):
        print(PromptText.TextChooseDifficulty)
        choose = 0
        while True:
            choose = get_input_option()
            if choose not in (1, 2, 3):
                print('please choose again')
                continue
        DataHandle.game_random_num(choose)
        # todo


def run():
    Game.init()
    if Game.game_login():
        print("login success")
    Game.start()
    pass


if __name__ == "__main__":
    run()
