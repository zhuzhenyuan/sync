print('='*20,'！欢迎来到唐僧大战白骨精游戏！','='*20)
print('请输入名称选择你的身份：')
print('='*66)
ts=1
bgj=2
print('    1.唐僧')
print('    2.白骨精')
nam=int(input('请选择：'))
#if nam==ts :
	#print('你将作为唐僧进行游戏！')
#if nam==bgj :
	#print('你选择的是白骨精，犯规！')
#else :
	#print('请在上面的名称中选择……')	
while nam!=ts :
	if nam!=bgj :
		print('='*66)
		print('就上面俩选项，你非得不一样，你咋这么秀呢')
		nam=input('请重新选择：')
	elif nam == bgj :
		print('='*66)
		print('白骨精是boos，boos是你要打的，你选了boos还打个球，重选！')
		nam=input('请重新选择：')
print('='*66)		
print('你将作为唐僧进行游戏！')
print('='*66)
t_hp=10
t_atk=1
b_hp=20
b_atk=5
print('选择你要进行的操作')
print('='*66)
print('唐僧的当前HP:',t_hp,' 唐僧的当前攻击力：',t_atk)
print('    1.练级','(HP+2  攻击力+1)')
lv=1
print('    2.打boos','(干他丫的白骨精！)')
pk=2
print('    3.逃跑','(溜了溜了……)')
run=3
i=int(input('请输入操作序号：'))
while i :	
	if i==lv :
		t_hp+=2
		t_atk+=1
		print('='*66)
		print('研习了大乘佛法','唐僧的当前HP:',t_hp,' 唐僧的当前攻击力：',t_atk)
		print('    1.练级','(HP+2  攻击力+1)')
		print('    2.打boos','(干他丫的白骨精！)')
		print('    3.逃跑','(溜了溜了……)')
		i=int(input('请输入操作序号：'))
	if i==pk :
		b_hp=b_hp-t_atk
		if b_hp>0 and t_atk<4:
			t_hp=t_hp-b_atk
			if t_hp>0 :
				print('='*66)
				print('对白骨精念经','白骨精受到了',t_atk,'点伤害！','唐僧的当前HP:',t_hp,' 唐僧的当前攻击力：',t_atk)
				print('    1.练级','(HP+2  攻击力+1)')
				print('    2.打boos','(干他丫的白骨精！)')
				print('    3.逃跑','(溜了溜了……)')
				i=int(input('请输入操作序号：'))
			else :
				print('='*66)
				print('你死了')
				break	
	if i==pk :	
		if b_hp>0 and t_atk<8:
			t_hp=t_hp-b_atk
			if t_hp>0 :
				print('='*66)
				print('用禅杖暴打了白骨精','白骨精受到了',t_atk,'点伤害！','唐僧的当前HP:',t_hp,' 唐僧的当前攻击力：',t_atk)
				print('    1.练级','(HP+2  攻击力+1)')
				print('    2.打boos','(干他丫的白骨精！)')
				print('    3.逃跑','(溜了溜了……)')
				i=int(input('请输入操作序号：'))
			else :
				print('='*66)
				print('你死了')
				break
		else :
			print('='*66)
			print('你击败了白骨精！')	
			break	
	if i==run :
		print('='*66)
		print('你逃跑了，游戏结束')
		break
input('请按回车结束游戏……')								
	