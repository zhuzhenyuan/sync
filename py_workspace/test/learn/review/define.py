import random
import csv

# 配表配置
enemys = {}


def read_config():
    # 读取敌人配置
    csv_reader = csv.reader(open("enemy.csv", encoding='UTF-8'))
    enemy_names = []
    i = 1
    for line in csv_reader:
        if i == 1:
            enemy_names = line
        elif i >= 3:
            d = {}
            for i in range(1, len(enemy_names)):
                if enemy_names[i] == "名字":
                    d[enemy_names[i]] = line[i]
                    continue
                d[enemy_names[i]] = int(line[i])  # 浮点数没有处理
            enemys[int(line[0])] = d
        i += 1


# 1.角色
class Role(object):
    def __init__(self, name):
        '''初始化角色属性'''
        self._name = name  # 名称
        self._hpMax = 10  # 生命上限
        self._hp = 0  # 当前生命
        self._atk = 0  # 攻击
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
        self._cri = self._luk / 100 + 1  # 暴击率
        self._hit = 1  # 命中率
        self._stun = False  # 晕眩状态
        self.skills = {1: '普通攻击'}
        # 通关数据
        self._esc = 0  # 逃跑次数
        self._dead = 0  # 死亡次数
        self._kill = 0  # 击杀次数
        self._begin = 0
        self._end = 0

    def add_hpMax(self, num=1):
        self._hpMax += num
        return max(self._hpMax, 1)

    def get_exp(self, num):
        self._exp += num + self._expbonus
        return max(self._exp, 0)

    def get_gold(self, num):
        self._gold += num + self._goldbonus
        return max(self._gold, 0)

    def print_bonus_panel(self):
        print('=' * 77)
        print(f'''{self._name}，请分配您的属性，当前剩余经验：{self._exp}\n
        				1   生命（需要{self._hpMax - 10}点经验）：  {self._hpMax}
        				2   攻击（需要{self._atk}点经验）：  {self._atk}
        				3   防御（需要{self._def}点经验）：  {self._def}
        				4   敏捷（需要{self._agi}点经验）：  {self._agi}
        				5   幸运（需要{self._luk}点经验）：  {self._luk}
        				6+  退出加点
        				''')

    def add_atr(self):
        attr_m = {
            2: '_atk',
            3: '_def',
            4: '_agi',
            5: '_luk',
        }

        def add_value(num, val):
            old_val = getattr(self, attr_m[num])
            if self._exp >= old_val:
                self._exp -= old_val
                setattr(self, attr_m[num], max(old_val + val, 0))
                return True
            return False

        while True:
            self.print_bonus_panel()
            try:
                atr_shuru = int(input('请输入选项数字\n'))
                if atr_shuru not in (1, 2, 3, 4, 5):
                    break
            except:
                print("try again")
                continue

            print('=' * 77)
            success = False
            if atr_shuru == 1:
                if self._exp >= (self._hpMax - 10):
                    self._exp -= (self._hpMax - 10)
                    self._hpMax += 1
                    success = True
            else:
                success = add_value(atr_shuru, 1)
            if not success:
                print("经验值不够哦")


def random_int(min_val, max_val):
    return random.randint(min_val, max_val)


# 2.敌人/怪物
class Enemy(object):
    '''初始化怪物属性'''

    def __init__(self, _id):
        self._id = int(_id)
        cfg = enemys[self._id]
        self._name = cfg['名字']
        self._level = cfg['难度']
        self._hp = 0
        self._hpMax = random_int(cfg['最低血量'], cfg['最高血量'])
        self._atk = random_int(cfg['最低攻击'], cfg['最高攻击'])
        self._def = random_int(cfg['最低防御'], cfg['最高防御'])
        self._agi = random_int(cfg['最低敏捷'], cfg['最高敏捷'])
        self._luk = random_int(cfg['最低幸运'], cfg['最高幸运'])
        self._stun = False  # 晕眩状态
        self.atk_chance = 1  # 攻击次数
        self._eva = min(self._agi / 100, 0.35) + float(cfg['基础闪避'])  # 闪避率
        self._cri = self._luk / 100  # 暴击率
        self._hit = float(cfg['基础命中'])  # 命中率
        self._exp = random_int(cfg['最低经验'], cfg['最高经验'])  # 击败后获得的经验
        self._gold = random_int(cfg['最低金币'], cfg['最高金币'])  # 击败后获得的金币

    def sux(self):
        sux_pool = ['脆弱的', '好运的', '强壮的', '善良的', '帅气的', '可爱的', '邪恶的']
        i = random_int(0, len(sux_pool) - 1)
        self._name = sux_pool[i] + self._name


read_config()
