import random
import csv
import colorama
from colorama import init, Fore, Back, Style

init(autoreset=True)
import os

os.system('')


def red(text):
    return '\033[31m' + str(text) + '\033[0m'


def green(text):
    return '\033[32m' + str(text) + '\033[0m'


def yellow(text):
    return '\033[33m' + str(text) + '\033[0m'


def blue(text):
    return '\033[34m' + str(text) + '\033[0m'


def light_blue(text):
    return '\033[36m' + str(text) + '\033[0m'


# 1.角色
class Role():
    def __init__(self, name):
        '''初始化角色属性'''
        self._name = name  # 名称
        self._hpMax = 10  # 生命上限
        self._hp = 0  # 当前生命
        self._atk = 10  # 攻击
        self._def = 0  # 防御
        self._agi = 0  # 敏捷
        self._luk = 0  # 幸运
        self._exp = 0  # 经验
        self._expbonus = 0  # 额外经验
        self._atr = 10  # 属性点
        self._hide_level = 1  # 动态等级
        self._gold = 0  # 金钱
        self._goldbonus = 0  # 额外金钱
        self.atk_chance = 1  # 攻击次数
        self._eva = min(self._agi / 100, 0.35)  # 闪避率
        self._cri = self._luk / 100  # 暴击率
        self._hit = 1  # 命中率
        self._stun = False  # 晕眩状态
        self.skills = {1: '普通攻击'}
        # 通关数据
        self._esc = 0  # 逃跑次数
        self._dead = 0  # 死亡次数
        self._kill = 0  # 击杀次数
        self._begin = 0
        self._end = 0
        # 优化内容
        self.attrs = {'hpMax': self._hpMax, 'atk': self._atk, 'def': self._def, 'agi': self._agi, 'luk': self._luk}
        self.attrs_list = list(self.attrs)

    def attr_print(self):
        print(f'{self.attrs_list}')

    def add_attr(self, attr, num=1):
        '''
        attr格式为'hpMax','atk','def','agi','luk'...
        '''
        self.attrs[attr] += num
        return max(self.attrs[attr], 0)

    # def add_hpMax(self,num=1) :
    # 	self._hpMax += num
    # 	return max(self._hpMax,1)
    # def add_atk(self,num=1) :
    # 	self._atk += num
    # 	return max(self._atk,0)
    # def add_def(self,num=1) :
    # 	self._def += num
    # def add_agi(self,num=1) :
    # 	self._agi += num
    # 	return max(self._agi,0)
    # def add_luk(self,num=1) :
    # 	self._luk += num
    # 	return max(self._luk,0)
    # def add_exp(self,num=1) :
    # 	self._exp += num
    # 	return max(self._exp,0)
    def get_exp(self, num):
        self._exp += num + self._expbonus
        return max(self._exp, 0)

    def get_gold(self, num):
        self._gold += num + self._goldbonus
        return max(self._gold, 0)

    def get_attr(self, attr):
        '''
        attr格式为'hpMax','atk','def','agi','luk'...
        '''
        return self.attrs[attr]

    def allo_atr(self):
        while True:
            print('=' * 77)
            print(f'''{light_blue(self._name)}，请分配您的属性，当前剩余经验：{self._exp}\n
				0   生命（需要{self._hpMax // 4}点经验）：  {self._hpMax}
				1   攻击（需要{self._atk}点经验）：  {self._atk}
				2   防御（需要{self._def}点经验）：  {self._def}
				3   敏捷（需要{self._agi}点经验）：  {self._agi}
				4   幸运（需要{self._luk}点经验）：  {self._luk}
				5+  退出加点
				''')
            atr_shuru = int(input('请输入选项数字\n'))
            print('=' * 77)
            for index in range(len(self.attrs_list)):
                if index == atr_shuru:
                    if index == 0:
                        if self._exp >= (self._hpMax // 4):
                            self._exp -= (self._hpMax // 4)
                            self._hpMax += 1
                            print('加点成功')
                        else:
                            print('经验值不够哦')
                    else:
                        if self._exp >= self.attrs[self.attrs_list[index]]:
                            self._exp -= self.attrs[self.attrs_list[index]]
                            self.attrs[self.attrs_list[index]] += 1
                            # self.add_attr(self.attrs_list[index])
                            print(f'{self.attrs[self.attrs_list[index]]}')
                            print('加点成功')
                        else:
                            print('经验值不够哦')
        # if atr_shuru == 1 :
        # 	if self._exp >= (self._hpMax//10) :
        # 		self._exp -= (self._hpMax//10)
        # 		self.add_hpMax()
        # 	else :
        # 		print('经验值不够哦')
        # elif atr_shuru == 2 :
        # 	if self._exp >= self._atk :
        # 		self._exp -= self._atk
        # 		self.add_atk()
        # 	else :
        # 		print('经验值不够哦')
        # elif atr_shuru == 3 :
        # 	if self._exp >= self._def :
        # 		self._exp -= self._def
        # 		self.add_def()
        # 	else :
        # 		print('经验值不够哦')
        # elif atr_shuru == 4 :
        # 	if self._exp >= self._agi :
        # 		self._exp -= self._agi
        # 		self.add_agi()
        # 	else :
        # 		print('经验值不够哦')
        # elif atr_shuru == 5 :
        # 	if self._exp >= self._luk :
        # 		self._exp -= self._luk
        # 		self.add_luk()
        # 	else :
        # 		print('经验值不够哦')
        # else :
        # 	break


# 读取敌人配置
csv_reader = csv.reader(open("enemy.csv", encoding='UTF-8'))
enemys = {}
enemy_names = []
i = 1
for line in csv_reader:
    if i == 1:
        enemy_names = line
    elif i >= 3:
        d = {}
        for i in range(1, len(enemy_names)):
            d[enemy_names[i]] = line[i]
        enemys[line[0]] = d
    i += 1


# 2.敌人/怪物
class Enemy():
    '''初始化怪物属性'''

    def __init__(self, _id):
        self._id = _id
        self._name = enemys[f'{self._id}']['名字']
        self._level = int(enemys[f'{self._id}']['难度'])
        self._hp = 0
        self._hpMax = random.randint(int(enemys[f'{self._id}']['最低血量']), int(enemys[f'{self._id}']['最高血量']))
        self._atk = random.randint(int(enemys[f'{self._id}']['最低攻击']), int(enemys[f'{self._id}']['最高攻击']))
        self._def = random.randint(int(enemys[f'{self._id}']['最低防御']), int(enemys[f'{self._id}']['最高防御']))
        self._agi = random.randint(int(enemys[f'{self._id}']['最低敏捷']), int(enemys[f'{self._id}']['最高敏捷']))
        self._luk = random.randint(int(enemys[f'{self._id}']['最低幸运']), int(enemys[f'{self._id}']['最高幸运']))
        self._stun = False  # 晕眩状态
        self.atk_chance = 1  # 攻击次数
        self._eva = min(self._agi / 100, 0.35) + float(enemys[f'{self._id}']['基础闪避'])  # 闪避率
        self._cri = self._luk / 100  # 暴击率
        self._hit = float(enemys[f'{self._id}']['基础命中'])  # 命中率
        self._exp = random.randint(int(enemys[f'{self._id}']['最低经验']), int(enemys[f'{self._id}']['最高经验']))  # 击败后获得的经验
        self._gold = random.randint(int(enemys[f'{self._id}']['最低金币']), int(enemys[f'{self._id}']['最高金币']))  # 击败后获得的金币

    def sux(self):
        sux_pool = ['脆弱的', '好运的', '强壮的', '善良的', '帅气的', '可爱的', '邪恶的']
        i = random.randint(0, len(sux_pool) - 1)
        self._name = sux_pool[i] + self._name

# guai_id = random.randint(1,4)
# guaiwu = Enemy(guai_id)
# guaiwu.sux()
# print(guaiwu._name)
# input()
