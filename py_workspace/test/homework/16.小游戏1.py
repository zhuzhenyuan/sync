# 小游戏 《唐僧大战白骨精》

# 显示欢迎信息
print('#'*20, '欢迎光临《唐僧大战白骨精》', '#'*20)

# 显示身份选择信息
print('请选择你的身份：')
print('\t1. 唐僧')
print('\t2. 白骨精')
# 游戏的身份选择
pl_ch = input('请选择[1-2]')

#
if pl_ch == '1':
    print('你已经选了1，将以唐僧身份游戏')
elif pl_ch == '2':
    print('对不起，你只能唐僧身份游戏，现在将以唐僧身份进行游戏~')
else:
    print('输入有误，系统将默认使用唐僧进行游戏')


# boss生命值，玩家生命值
boss_hp = 10
pl_hp = 2
# boss攻击力，玩家攻击力
boss_att = 1
pl_att = 2
print('#'*66)
# 显示玩家信息
print(f'唐僧，你的生命值是{pl_hp}, 你的攻击力是{pl_att}')

while True:
    #
    print('#'*66)
    #
    print('请选择要进行操作：')
    print('\t1.练级')
    print('\t2.打怪')
    print('\t3.跑路')
    game_ch = input('请选择要进行的操作[1-3]:')

    if game_ch == '1':
        pl_hp += 2
        pl_att += 2
        print(f'恭喜你升级了! 你现在的生命值是{pl_hp}, 攻击力是{pl_att}')
    elif game_ch == '2':
        boss_hp -= pl_att
        pl_hp -= boss_att
        if boss_hp <= 0:
            print(f'boss已死亡，ヾ(￣ー￣)X(^▽^)ゞ, 恭喜通关！！！~~~~~')
            break
        elif pl_hp <= 0:
            print(f'你已躺尸，请升级后再来尝试~')
        else:
            print(f'对boss造成了{pl_att}点伤害，boss剩余血量为{boss_hp}')
    elif game_ch ==3:
        print('跑路了跑路了~~~')

