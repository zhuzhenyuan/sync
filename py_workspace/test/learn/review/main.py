import random
import define
import time


# 通关
def over(player):
    all_time = player.end - player.begin
    hour = int(all_time // 3600)
    minute = int((all_time - hour * 3600) // 60)
    second = int(all_time - hour * 3600 - minute * 60)
    time = f'{hour}时{minute}分{second}秒'
    print('=' * 66)
    print(f'''你击败了最终的邪恶，权权龙向你求饶，并放了村长的老婆……
但是邪恶的气息并没有减弱，反而愈加浓烈，也许，事情没有这么简单……
to be continued...
		通关用时：{time}，打败了92.368%的玩家
		失败次数：{player._dead}
		逃跑成功：{player._esc}
		击杀次数：{player._kill}''')
    print('=' * 66)
    input('任意按键结束游戏')
    exit()


# 战斗
def combat():
    level = min(int(player._hide_level / 10) + 1, 4)
    guai_id = random.randint(1, level)
    guaiwu = define.Enemy(guai_id)
    guaiwu.sux()
    print('=' * 77)
    flag = True
    taopao = True
    while flag:
        print(f'''{rName}在野外遇到了{guaiwu._name}\n
			1.查看属性
			2.开始战斗
			3+.尝试逃跑
			''')
        choice = input('请输入选项数字\n')
        print('=' * 77)
        if choice == '1':
            print('=' * 77)
            print(f'''
				{guaiwu._name}的属性如下：\n
				生命值：{guaiwu._hpMax}
				攻击：{guaiwu._atk}
				防御：{guaiwu._def}
				敏捷：{guaiwu._agi}
				幸运：{guaiwu._luk}
				''')
            print('=' * 77)
        elif choice == '2':
            '''战斗流程'''
            s1 = '%s对%s使用了%s，'
            s2 = '造成了%d点伤害'
            s3 = '%s被击败了'
            player._hp = player._hpMax
            guaiwu._hp = guaiwu._hpMax
            while True:
                if player._agi >= guaiwu._agi:
                    '''勇者行动'''
                    damage = int(max((player._atk + random.randint(0, player._luk) - guaiwu._def), 1))
                    if random.random() > (player._hit - guaiwu._eva):
                        txt1 = '失手了！'
                        damage *= 0
                        print(s1 % (player._name, guaiwu._name, '普通攻击') + txt1 + s2 % (damage))
                    else:
                        if random.random() <= player._cri:
                            txt2 = '命中要害了！'
                            damage *= 2
                            print(s1 % (player._name, guaiwu._name, '普通攻击') + txt2 + s2 % (damage))
                        else:
                            print(s1 % (player._name, guaiwu._name, '普通攻击') + s2 % (damage))
                    guaiwu._hp -= damage
                    if guaiwu._hp <= 0:
                        if guai_id == 3:
                            player.end = time.time()
                            over(player)
                            flag = False
                            break
                        else:
                            print(s3 % guaiwu._name, f'，获得了{guaiwu._exp}经验和{guaiwu._gold}金币')
                            player._exp += guaiwu._exp
                            player._gold += guaiwu._gold
                            player._hide_level += guaiwu._level
                            flag = False
                            player._kill += 1
                            break
                    '''怪物行动'''
                    damage = int(max((guaiwu._atk + random.randint(0, guaiwu._luk) - player._def), 1))
                    if random.random() > (guaiwu._hit - player._eva):
                        txt1 = '失手了！'
                        damage *= 0
                        print(s1 % (guaiwu._name, player._name, '普通攻击') + txt1 + s2 % (damage))
                    else:
                        if random.random() <= guaiwu._cri:
                            txt2 = '命中要害了！'
                            damage *= 2
                            print(s1 % (guaiwu._name, player._name, '普通攻击') + txt2 + s2 % (damage))
                        else:
                            print(s1 % (guaiwu._name, player._name, '普通攻击') + s2 % (damage))
                    player._hp -= damage
                    if player._hp <= 0:
                        print(s3 % player._name, '再醒来时，已经躺在了村长的怀里，仿佛之前的一切只是一场梦')
                        player._hide_level -= 1
                        player._hide_level = max(player._hide_level, 1)
                        flag = False
                        player._dead += 1
                        break
                else:
                    '''怪物行动'''
                    damage = int(max((guaiwu._atk + random.randint(0, guaiwu._luk) - player._def), 1))
                    if random.random() > (guaiwu._hit - player._eva):
                        txt1 = '失手了！'
                        damage *= 0
                        print(s1 % (guaiwu._name, player._name, '普通攻击') + txt1 + s2 % (damage))
                    else:
                        if random.random() <= guaiwu._cri:
                            txt2 = '命中要害了！'
                            damage *= 2
                            print(s1 % (guaiwu._name, player._name, '普通攻击') + txt2 + s2 % (damage))
                        else:
                            print(s1 % (guaiwu._name, player._name, '普通攻击') + s2 % (damage))
                    player._hp -= damage
                    if player._hp <= 0:
                        print(s3 % player._name, '再醒来时，已经躺在了村长的怀里，仿佛之前的一切只是一场梦')
                        player._hide_level -= 1
                        player._hide_level = max(player._hide_level, 1)
                        flag = False
                        player._dead += 1
                        break
                    '''勇者行动'''
                    damage = int(max((player._atk + random.randint(0, player._luk) - guaiwu._def), 1))
                    if random.random() > (player._hit - guaiwu._eva):
                        txt1 = '失手了！'
                        damage *= 0
                        print(s1 % (player._name, guaiwu._name, '普通攻击') + txt1 + s2 % (damage))
                    else:
                        if random.random() <= player._cri:
                            txt2 = '命中要害了！'
                            damage *= 2
                            print(s1 % (player._name, guaiwu._name, '普通攻击') + txt2 + s2 % (damage))
                        else:
                            print(s1 % (player._name, guaiwu._name, '普通攻击') + s2 % (damage))
                    guaiwu._hp -= damage
                    if guaiwu._hp <= 0:
                        if guai_id == 3:
                            player.end = time.time()
                            over(player)
                            flag = False
                            break
                        else:
                            print(s3 % guaiwu._name, f'，获得了{guaiwu._exp}经验和{guaiwu._gold}金币')
                            player._exp += guaiwu._exp
                            player._gold += guaiwu._gold
                            player._hide_level += guaiwu._level
                            flag = False
                            player._kill += 1
                            break
        else:
            '''逃跑流程'''
            if taopao:
                if random.random() <= (player._agi / 2 * guaiwu._agi):
                    print('逃跑成功')
                    player._esc += 1
                    break
                else:
                    print('逃跑失败')
                    taopao = False
            else:
                print('你还想逃到哪去呢？')


def print_banner():
    # 游戏主体
    print('===============================《套套斗恶龙》v0.0.2=============================')
    print('==================================龙龙恶狗！==================================')
    print('==================================天生异象！==================================')
    print('==================================无名小村！==================================')
    print('==================================勇者降生！==================================')
    print('''v0.0.2新增内容：
        1.增加怪物数量
        2.战斗加了暴击和闪避
        3.增加无意义的通关
        4.增加无意义的通关数据显示''')
    print('=' * 77)


def create_player():
    # 名称输入
    while True:
        print('给这个小baby取个什么名字呢？')
        rName = input('请输入你想取的名称：\n')
        if len(rName) <= 0:
            continue
        name_queren = input(f'叫你{rName}可以吗？1：确认 2+：取消 \n')
        if name_queren == '1':
            break
    if rName:
        player = define.Role(rName)
        player.begin = time.time()
        return player


if __name__ == "__main__":
    print_banner()
    player = create_player()
    # 初始属性分配
    ss3 = '加点成功，属性点已用完，自动退出加点'
    ss4 = '不能有属性为0，加点失败'
    ss8 = '您没有这么多属性点呢'
    while True:
        print('=' * 77)
        print(f'''可爱的{player._name}，请分配您的初始属性，剩余可用属性点：{player._atr}\n
            -1+   生命：  {player._hpMax}
            -2+   攻击：  {player._atk}
            -3+   防御：  {player._def}
            -4+   敏捷：  {player._agi}
            -5+   幸运：  {player._luk}
            ''')
        atr_shuru = input('请输入加点，格式[数字+/-]\n')
        print('=' * 77)
        if atr_shuru not in ('1+', '2+', '3+', '4+', '5+', '1-', '2-', '3-', '4-', '5-'):
            print("try again")
            continue
        try:
            if '+' in atr_shuru:
                num = int(input('请输入要增加的点数'))
                if num > player._atr:
                    print('属性点不够用了')
                    continue
            else:
                if player._hpMax <= 0:
                    print('无法再降低了')
                    continue
                num = int(input('请输入要降低的点数'))
            # 后面得变量名都可以用num代替
        except:
            print('输入有误')
            continue

        if atr_shuru == '1+':
            llup = num
            player._atr -= llup
            if player._atr == 0:
                if player._atk * player._def * player._agi * player._luk != 0:
                    player._hpMax += llup
                    print(ss3)
                    break
                else:
                    player._atr += llup
                    print(ss4)
                    continue
            else:
                player._hpMax += llup
                print(f'加点成功，你的生命提升{llup}')

        elif atr_shuru == '1-':
            lldown = num
            if lldown > player._hpMax:
                print(ss8)
            else:
                player._atr += lldown
                player._hpMax -= lldown
                print(f'加点成功，你的生命降低{lldown}')
        elif atr_shuru == '2+':
            tzup = num
            player._atr -= tzup
            if player._atr == 0 and player._hpMax * player._def * player._agi * player._luk != 0:
                player._atk += tzup
                print(ss3)
                break
            elif player._atr == 0 and player._hpMax * player._def * player._agi * player._luk == 0:
                player._atr += tzup
                print(ss4)
                continue
            else:
                player._atk += tzup
                print(f'加点成功，你的攻击提升{tzup}')
        elif atr_shuru == '2-':
            tzdown = num
            if tzdown > player._atk:
                print(ss8)
            else:
                player._atr += tzdown
                player._atk -= tzdown
                print(f'加点成功，你的攻击降低{tzdown}')
        elif atr_shuru == '3+':
            mjup = num
            player._atr -= mjup
            if player._atr == 0 and player._hpMax * player._atk * player._agi * player._luk != 0:
                player._def += mjup
                print(ss3)
                break
            elif player._atr == 0 and player._hpMax * player._atk * player._agi * player._luk == 0:
                player._atr += mjup
                print(ss4)
                continue
            else:
                player._def += mjup
                print(f'加点成功，你的防御提升{mjup}')
        elif atr_shuru == '3-':
            mjdown = num
            if mjdown > player._def:
                print(ss8)
            else:
                player._atr += mjdown
                player._def -= mjdown
                print(f'加点成功，你的防御降低{mjdown}')
        elif atr_shuru == '4+':
            zlup = num
            player._atr -= zlup
            if player._atr == 0 and player._hpMax * player._atk * player._def * player._luk != 0:
                player._agi += zlup
                print(ss3)
                break
            elif player._atr == 0 and player._hpMax * player._atk * player._def * player._luk == 0:
                player._atr += zlup
                print(ss4)
                continue
            else:
                player._agi += zlup
                print(f'加点成功，你的敏捷提升{zlup}')
        elif atr_shuru == '4-':
            zldown = num
            if zldown > player._agi:
                print(ss8)
            else:
                player._atr += zldown
                player._agi -= zldown
                print(f'加点成功，你的敏捷降低{zldown}')
        elif atr_shuru == '5+':
            jsup = num
            player._atr -= jsup
            if player._atr == 0 and player._hpMax * player._atk * player._def * player._agi != 0:
                player._luk += jsup
                print(ss3)
                break
            elif player._atr == 0 and player._hpMax * player._atk * player._def * player._agi == 0:
                player._atr += jsup
                print(ss4)
                continue
            else:
                player._luk += jsup
                print(f'加点成功，你的幸运提升{jsup}')
        elif atr_shuru == '5-':
            jsdown = num
            if jsdown > player._luk:
                print(ss8)
            else:
                player._atr += jsdown
                player._luk -= jsdown
                print(f'加点成功，你的幸运降低{jsdown}')

    # 探索内容
    print(f'村长说他的老婆被恶龙抓走了，于是可爱的{rName}便开始了打怪拯救村长老婆之旅')
    while True:
        # try :
        print(f'可爱的{rName}，你来到了野外，你要……')
        print('1.打怪')
        print('2.扎营升级')
        print('3+.退出游戏')
        print('=' * 77)
        r_choice = int(input('输入选项序号: '))
        if r_choice == 1:
            combat()
        elif r_choice == 2:
            player.add_atr()
        else:
            print('游戏结束，点击右上角叉号关闭该游戏')
            break
    # except :
    # 	print('看不懂中文是吧？叫你输入选项序号，有这序号吗？')
