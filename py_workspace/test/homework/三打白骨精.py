#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      PM
#
# Created:     06/12/2021
# Copyright:   (c) PM 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("-"*20 , '欢迎来到《三打白骨精》', "-"*20)
print('请选择你的身份：')
print('\t1.猪八戒')
print('\t2.孙悟空')
##1.身份选择
print("-"*64)
paly = input('请选择[1-2]')
##用户的选择
if paly == "1" :
    print('你选择了--》猪八戒《--进行游戏')
elif paly == "2":
    print('你选择了--》孙悟空《--进行游戏，太强了不能选，强制进行切换至--》猪八戒《--')
else :
    print('抱歉你选择了无效选项，系统将强制进行切换至--》猪八戒《--')

##2.玩法设计
##显示玩家信息（血、命）
play_atk = 2
play_hp = 2
boss_atk = 10
boss_hp = 10
print("-"*64)
print(f'猪八戒，你的生命值{play_hp}，你的攻击力{play_atk}')

##游戏开始
while True :
    print('请选择你的操作：')
    print('\t1.练级')
    print('\t2.打怪')
    print('\t3.逃跑')
    paly = input('请选择[1-3]')
    print("-"*64)
    if paly == "1" :
        play_atk += 2
        play_hp += 2
        print(f'打怪获得经验升级成功！！！你的生命值{play_hp}，你的攻击力{play_atk}')
    elif paly == "2" :
        if boss_hp < play_atk :
            boss_hp -= play_atk
            if boss_hp <= 0 :
                print(f'--》猪八戒《--攻击了--》白骨精《--，对手太弱了，直接秒杀')
                print('-'*20,'恭喜玩家通关游戏','-'*20)
                break
        else :
            play_hp -= boss_atk
            if play_hp <= 0 :
                print(f'--》猪八戒《--攻击了--》白骨精《--，等级不足，直接被秒杀')
                print('-'*20,'很遗憾游戏结束，继续加油┗|｀O′|┛ 嗷~~','-'*20)
                while True :
                    paly = input('请选择[1-3]')
                    if paly == "1" :
                        play_atk += 2
                        play_hp += 2
                        print(f'获得经验升级成功！！！你的生命值{play_hp}，你的攻击力{play_atk}')
                        paly = input('请选择[1-3]')
                    elif paly == "2" :
                        boss_hp -= play_atk
                        if boss_hp <= 0 :
                            print('--》猪八戒《--攻击了--》白骨精《--，对手太弱了，直接秒杀')
                            print('-'*20,'恭喜玩家通关游戏','-'*20)
                            break
                    break
    else :
        print('--》猪八戒《--躲在草丛里呼呼大睡')
















