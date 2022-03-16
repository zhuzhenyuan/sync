# coding:utf8
import os
import random
import json
import time
from xml.sax.handler import DTDHandler
import requests


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


# 数据处理类
class DataHandle(object):

    @classmethod
    def exit_game(cls):
        requests.get("http://127.0.0.1:9999/game/exit")
        exit(0)

    @classmethod
    def handler_game_login(cls, choose, username, passwd):
        ret = requests.get("http://127.0.0.1:9999/game/login", {'args': (choose, username, passwd)})
        print(ret.json()['args'])
        return ret.json()['args']

    @classmethod
    def game_random_num(cls, username, difficulty):
        ret = requests.get("http://127.0.0.1:9999/game/random", {'args': (username, difficulty)})
        return ret.json()['args']
    
    @classmethod
    def game_check_num(cls, username, num):
        ret = requests.get("http://127.0.0.1:9999/game/check", {'args': (username, num)})
        return ret.json()['args']

    @classmethod
    def game_get_info(cls, username):
        ret = requests.get("http://127.0.0.1:9999/game/info", {'args': (username)})
        return ret.json()['args']

    @classmethod
    def game_get_points_leaderboard(cls):
        ret = requests.get("http://127.0.0.1:9999/game/leaderboard/points")
        return ret.json()['args']
    
    @classmethod
    def game_get_frequency_leaderboard(cls):
        ret = requests.get("http://127.0.0.1:9999/game/leaderboard/frequency")
        return ret.json()['args']


class Game(object):
    @classmethod
    def game_login(cls):
        op_pages = {
            1: Pages.login_page,
            2: Pages.register_page,
            3: DataHandle.exit_game,
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
            4: DataHandle.exit_game,
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
    username = Game.game_login()
    if username:
        print("login success")
    Game.start(username)


if __name__ == "__main__":
    run()
    # ret = requests.get("http://127.0.0.1:9999/game/login", {'args': (1, 'zzy', '1234')})
    # print(ret.json()['args'])
