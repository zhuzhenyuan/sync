# 显示欢迎信息
a = '冷兔'
b = '龙喵'
c = '喵喵'
print('='*20,f'欢迎光临《{a}大战{b}》','='*20)

print('请选择你的身份')
print(f'\t1.{a}')
print(f'\t2.{b}')
# 根据用户选择不同信息
player_choose = input('请选择[1-2]:')
print('-'*40)
if player_choose == '1':
	print(f'你选择了-{a}-的身份进入游戏')
elif player_choose == '2':
	print(f'你选择了-{b}-的身份进入游戏')
else:
	print(f'恭喜你解锁影藏的身份-{c}-进入游戏')
# 进入游戏

player_hp = 2 #初始生命值
player_attack = 2 #初始攻击力
boss_hp = 10 #BOSS生命值
boss_attack = 10 #BOSS攻击力
print('-'*40)
print(f'你的初始生命值：{player_hp} ,你的初始攻击力是：{player_attack}')
# 循环游戏操作
while True:
	print('-'*40)
	print('\t1.吃饭')
	print('\t2.玩游戏')
	print('\t2.看剧')
	game_choose_01 = input('请选择[1-3]:')
	if game_choose_01 == '1':
		player_hp += 2
		player_attack += 2
		print('-'*40)
		print(f'玩玩玩！恭喜升级！你现在的生命值是：{player_hp} ,你现在的攻击力是：{player_attack}')
	elif game_choose_01 == '2':
			boss_hp -= player_attack
			print('-'*40)
			if boss_hp <= 0:
				print(f'BOSS生命值受到了{player_attack}伤害，BOSS死亡，玩家胜利！')
				break
			player_hp -= boss_attack
			if player_hp <= 0:
				print(f'你受到了{player_attack}伤害，啊这人没了！')
				break
	elif game_choose_01 == '3':
		print('去呗！游戏结束！')
	else :
		print('输入有误，请重新输入')