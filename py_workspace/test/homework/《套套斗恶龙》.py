# 1.身份选择
# 1.1 显示提示信息
# 1.2 用户选择身份
import random
print('===============================《套套斗恶龙》v0.0.1=============================')
print('==================================龙龙恶狗！==================================')
print('==================================天生异象！==================================')
print('==================================无名小村！==================================')
print('==================================勇者降生！==================================')
print('给这个小baby取个什么名字呢？')
print('1.套套')
print('2.小套套')
print('3.套套子')
try :
	r_name = int(input('输入选项序号: '))
	if r_name == 1 :
		rName = '套套'
	elif r_name == 2 :
		rName = '小套套'
	elif r_name == 3 :
		rName = '套套子'
	else :
		print('系统判断这孩子智商不行，自动分配名称"套狗蛋"')
		rName = '套狗蛋'
except :
	print('系统判断这孩子智商不行，自动分配名称"套狗蛋"')
	rName = '套狗蛋'
attack = random.randint(1,6)
defence = random.randint(1,6)
agile = random.randint(1,6)
luck = random.randint(1,6)
hpMax = random.randint(5,20)
exp = 0
print(f'==可爱的{rName}，系统已为您生成随机属性，生命：{hpMax}，攻击：{attack}，防御：{defence}，敏捷：{agile}，幸运：{luck}')
# 2.游戏主体
# 2.1 显示玩家基本信息
print(f'村长说他的老婆被恶龙抓走了，于是可爱的{rName}便开始了打怪拯救村长老婆之旅')
# 2.2 显示玩家可以进行的操作
print(f'==可爱的{rName}，你来到了野外，你要……')
# 	1.升级
# 	2.打怪
# 	怪物或玩家是否被消灭
# 	游戏结束
# 	3.逃跑
# 	退出游戏，显示提示信息
while True :
	try :
		print('1.打怪')
		print('2.扎营升级')
		print('3+.退出游戏')
		print('='*77)
		r_choice = int(input('输入选项序号: '))
		if r_choice == 1 :
			monsterID = random.randint(1,3)
			if monsterID == 1 :
				attack1 = random.randint(1,3)
				defence1 = random.randint(1,3)
				agile1 = random.randint(1,3)
				luck1 = random.randint(1,3)
				hp1 = random.randint(3,6)
				print(f'你当前的属性为，生命：{hpMax}，攻击：{attack}，防御：{defence}，敏捷：{agile}，幸运：{luck}')
				print(f'你遇到了小小怪：呸呸子，生命：{hp1}，攻击：{attack1}，防御：{defence1}，敏捷：{agile1}，幸运：{luck1}')
				hp = hpMax
				while hp > 0 and hp1 > 0 :
					if agile >= agile1 :
						shanghai = max((attack - defence1),1)+random.randint(1,luck)
						print(f'{rName}对呸呸子发起了攻击，造成了{shanghai}点伤害')
						hp1 -= shanghai
						if hp1 <= 0 :
							exp1 = random.randint(3,6)
							print(f'你击败了呸呸子，获得了{exp1}经验值')
							exp += exp1
							break
						shanghai1 = max((attack1 - defence),1)+random.randint(1,luck1)
						print(f'呸呸子对{rName}发起了攻击，造成了{shanghai1}点伤害')
						hp -= shanghai1
						if hp <= 0 :
							print('很遗憾，你死在了弱不禁风的呸呸子手下')
							break
					else :
						shanghai1 = max((attack1 - defence),1)+random.randint(1,luck1)
						print(f'呸呸子对{rName}发起了攻击，造成了{shanghai1}点伤害')
						hp -= shanghai1
						if hp <= 0 :
							print('很遗憾，你死在了弱不禁风的呸呸子手下')
							break
						shanghai = max((attack - defence1),1)+random.randint(1,luck)
						print(f'{rName}对呸呸子发起了攻击，造成了{shanghai}点伤害')
						hp1 -= shanghai
						if hp1 <= 0 :
							exp1 = random.randint(3,6)
							print(f'你击败了呸呸子，获得了{exp1}经验值')
							exp += exp1
							break
			elif monsterID == 2 :
				attack2 = random.randint(3,9)
				defence2 = random.randint(3,9)
				agile2 = random.randint(3,9)
				luck2 = random.randint(3,9)
				hp2 = random.randint(5,15)
				print(f'你当前的属性为，生命：{hpMax}，攻击：{attack}，防御：{defence}，敏捷：{agile}，幸运：{luck}')
				print(f'你遇到了精英怪：航航子，生命：{hp2}，攻击：{attack2}，防御：{defence2}，敏捷：{agile2}，幸运：{luck2}')
				hp = hpMax
				shanghai = 0
				shanghai1 = 0
				while hp > 0 and hp2 > 0 :
					if agile >= agile2 :
						shanghai = max((attack - defence2),1)+random.randint(1,luck)
						print(f'{rName}对航航子发起了攻击，造成了{shanghai}点伤害')
						hp2 -= shanghai
						if hp2 <= 0 :
							exp2 = random.randint(5,10)
							print(f'你击败了航航子，获得了{exp2}经验值')
							exp += exp2
							break
						shanghai1 = max((attack2 - defence),1)+random.randint(1,luck2)
						print(f'航航子对{rName}发起了攻击，造成了{shanghai1}点伤害')
						hp -= shanghai1
						if hp <= 0 :
							print('很遗憾，你死在了有点厉害的航航子手下')
							break
					else :
						shanghai1 = max((attack2 - defence),1)+random.randint(1,luck2)
						print(f'航航子对{rName}发起了攻击，造成了{shanghai1}点伤害')
						hp -= shanghai1
						if hp <= 0 :
							print('很遗憾，你死在了有点厉害的航航子手下')
							break
						shanghai = max((attack - defence2),1)+random.randint(1,luck)
						print(f'{rName}对航航子发起了攻击，造成了{shanghai}点伤害')
						hp2 -= shanghai
						if hp2 <= 0 :
							exp2 = random.randint(5,10)
							print(f'你击败了航航子，获得了{exp2}经验值')
							exp += exp2
							break
			else :
				attack3 = random.randint(5,15)
				defence3 = random.randint(0,1)
				agile3 = random.randint(0,1)
				luck3 = random.randint(1,1)
				hp3 = random.randint(30,50)
				print(f'你当前的属性为，生命：{hpMax}，攻击：{attack}，防御：{defence}，敏捷：{agile}，幸运：{luck}')
				print(f'你遇到了超级无敌邪恶大BOSS：权权龙，生命：{hp3}，攻击：{attack3}，防御：{defence3}，敏捷：{agile3}，幸运：{luck3}')
				hp = hpMax
				shanghai = 0
				shanghai1 = 0
				while hp > 0 and hp3 > 0 :
					if agile >= agile3 :
						shanghai = max((attack - defence3),1)+random.randint(1,luck)
						print(f'{rName}对权权龙发起了攻击，造成了{shanghai}点伤害')
						hp3 -= shanghai
						if hp3 <= 0 :
							exp3 = random.randint(10,20)
							print(f'你击败了权权龙，获得了{exp3}经验值')
							exp += exp3
							break
						shanghai1 = max((attack3 - defence),1)+random.randint(1,luck3)
						print(f'权权龙对{rName}发起了攻击，造成了{shanghai1}点伤害')
						hp -= shanghai1
						if hp <= 0 :
							print('很遗憾，你死在了大BOSS权权龙的爪下')
							break
					else :
						shanghai1 = max((attack3 - defence),1)+random.randint(1,luck3)
						print(f'权权龙对{rName}发起了攻击，造成了{shanghai1}点伤害')
						hp -= shanghai1
						if hp <= 0 :
							print('很遗憾，你死在了有点厉害的权权龙手下')
							break
						shanghai = max((attack - defence3),1)+random.randint(1,luck)
						print(f'{rName}对权权龙发起了攻击，造成了{shanghai}点伤害')
						hp3 -= shanghai
						if hp3 <= 0 :
							exp3 = random.randint(10,20)
							print(f'你成功打败了大BOSS权权龙，村长老婆也一起殉情了，你获得了{exp3}经验值')
							exp += exp3
							break
		elif r_choice == 2 :
			while True:
				try :
					print(f'1.升级血量，需要花费{int(hpMax/2)}经验值')
					print(f'2.升级攻击，需要花费{attack}经验值')
					print(f'3.升级防御，需要花费{defence}经验值')
					print(f'4.升级敏捷，需要花费{agile}经验值')
					print(f'5.升级幸运，需要花费{luck}经验值')
					print(f'6+.退出升级')
					print(f'你目前可用的经验值为{exp}')
					print('='*77)
					r_choice2 = int(input('输入选项序号: '))
					if r_choice2 == 1 :
						if exp >= int(hpMax/2) :
							exp -= int(hpMax/2)
							hpMax += 1
							print(f'升级后你的血量为{hpMax}，剩余经验值为{exp}')
						else :
							print('经验值不够呢亲')
					elif r_choice2 == 2 :
						if exp >= attack :
							exp -= attack
							attack += 1
							print(f'升级后你的攻击为{attack}，剩余经验值为{exp}')
						else :
							print('经验值不够呢亲')
					elif r_choice2 == 3 :
						if exp >= defence :
							exp -= defence
							defence += 1
							print(f'升级后你的防御为{defence}，剩余经验值为{exp}')
						else :
							print('经验值不够呢亲')
					elif r_choice2 == 4 :
						if exp >= agile :
							exp -= agile
							agile += 1
							print(f'升级后你的敏捷为{agile}，剩余经验值为{exp}')
						else :
							print('经验值不够呢亲')
					elif r_choice2 == 5 :
						if exp >= luck :
							exp -= luck
							luck += 1
							print(f'升级后你的幸运为{luck}，剩余经验值为{exp}')
						else :
							print('经验值不够呢亲')
					else :
						break
				except :
					print('看不懂中文是吧？叫你输入选项序号，有这序号吗？')
		else :
			print('游戏结束，点击右上角叉号关闭该游戏')
			break
	except :
		print('看不懂中文是吧？叫你输入选项序号，有这序号吗？')