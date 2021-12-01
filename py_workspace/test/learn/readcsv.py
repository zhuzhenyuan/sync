
# csv 其实就是一个 文本文件，可以直接读
# open 文件操作， ./data.csv 相对路径
# with open("../learn/data.csv") as f:
# 	for line in f:  # 遍历每行
# 		print(line)
#
#
# import csv  # 导入库
# csv_reader = csv.reader(open("./data.csv"))
# for line in csv_reader:
# 	print(line)

import math

a1, a2 = 10, 3
b1, b2 = -10, 3

print("向上取整, 趋向正无穷")
print("%d / %d = %d" % (a1, a2, math.ceil(a1/a2)))
print("%d / %d = %d" % (b1, b2, math.ceil(b1/b2)))

print("向下取整，趋向负无穷")
print("%d / %d = %d" % (a1, a2, math.floor(a1/a2)))
print("%d / %d = %d" % (b1, b2, math.floor(b1/b2)))

print("截断小数，趋向零")
print("%d / %d = %d" % (a1, a2, int(a1/a2)))
print("%d / %d = %d" % (b1, b2, int(b1/b2)))

print("python中得除法取整采用 向下取整 的方式")
print("%d / %d = %f" % (a1, a2, a1/a2))
print("%d // %d = %f" % (a1, a2, a1//a2))
print("%d / %d = %f" % (b1, b2, b1/b2))
print("%d // %d = %f" % (b1, b2, b1//b2))

print()

print('例子1')
a1, a2 = -11, 5
print(a1 // a2)
print(a1 - (a1 // a2) * a2)

print('例子2')
a1, a2 = 10.2, 3
print(a1 // a2)
print(a1 - (a1 // a2) * a2)

'''
取余推导
a1 = a2 * n + r
n = a1 // a2
==> a1 = (a1 // a2) * a2 + r
==> r = a1 - (a1 // a2) * a2
'''

'''
浮点数不能想整数一样在计算机中准确表示
所以在比较浮点数时，一般计算差值，误差在可接受范围内即相等
例如 
a = 2
b = 1.99999999999999999
(a-b) < 0.00000000001 ==> a = b
'''


# a = 1
# b = 1
# c = 2
# d = []
# e = []
# print("查看变量地址")
# print("a = " + str(a) + ", address => " + str(id(a)))
# print("b = " + str(b) + ", address => " + str(id(b)))
# print("c = " + str(c) + ", address => " + str(id(c)))
# print("d = " + str(d) + ", address => " + str(id(d)))
# print("e = " + str(e) + ", address => " + str(id(e)))
#
#
# print("查看变量占用大小")
# import sys
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof([]))


