print('-'*10,'欢迎挑战小林林','-'*10)
print('请选择你的武器：')
print('1.粉色充气锤')
print('2.美味椰奶')
print('3.辣椒炒肉')
ss_choose = input('我选择：')
print('='*40)
if ss_choose == '1' :
	print('你选择了 >-粉色充气锤-< ')
	print('='*40)
	chui_atk = 1
	ss_life = 2
	ss_atk = 2
	ll_life = 10
	ll_atk = 10
	print(f'你的生命值是:{ss_life}，你的攻击力是：{ss_atk}，粉色充气锤为你额外提供：{chui_atk} 的攻击力')
	print('='*40)
	while True :
		print('接下来你要做什么：')
		print('1.挑战小林林')
		print('2.锻炼肉体')
		print('3.升级武器')
		print('4.逃跑')
		c_1 = input('：')
		print('='*40)
		if c_1 =='1' :
			ll_life -= ss_atk + chui_atk
			print(f'你用小锤攻击了小林林，小林林受到了 {ss_atk + chui_atk} 点伤害。')
			if ll_life <= 0 :
				print(f'小林林的生命值为{ll_life} ，无法再战斗了，决定向你投降')
				break
			else :
				ss_life -= ll_atk
				print(f'林林攻击了你，好痛！你受到了{ll_atk}点伤害')
				if ss_life <= 0 :
					print(f'你的生命为{ss_life}你失败了，game over')
					break
		elif c_1 == '2' :
			ss_life += 2 
			ss_atk += 2
			print(f'恭喜你的生命提升为{ss_life},攻击力提升为{ss_atk}')
			print('='*40)
		elif c_1 == '3' :
			chui_atk += 2
			print(f'你给充气锤填充了更多的气体，攻击力提升为{chui_atk}')
		elif c_1 == '4' :
			print('你被小林林抓住了，一辈子别想离开，game over')
			break
		else :
			print('你被小林林抓住了，一辈子别想离开，game over')	
			break

elif ss_choose == '2' :
	print('小林林抢走了你的椰奶，你失去了武器，game over.')
elif ss_choose == '3' :
	print('你吃完辣椒炒肉不想挑战小林林了，game over.')
else :
	print('你赤手空拳，太弱小了，给你一把 >-粉色充气锤-< 好了')
