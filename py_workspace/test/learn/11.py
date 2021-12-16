# contine break是用于控制循环体，使用取决于需求。
# 只要最终能够跳出循环即刻，除非需求是死循环
# 例
# import time
# i = 0
# while True:  # 死循环
#     i += 1  # 一个变化的变量，最终可以跳出循环
#     if i == 5:
#         continue
#     print(i)
#     time.sleep(0.5)
#
#     if i == 10:
#         break

# a1 = "姓名"
# a2 = "年龄"
# a3 = "性别"
# a4 = "住址"
#
# b1 = "小兰"
# b2 = "20"
# b3 = "男"
# b4 = "10号街道"
#
# tab = '\t'
# s = f"{a1}  {a2}{tab}{a3}{tab}{a4}"
# s2 = f"{b1}{tab}{b2}{tab}{b3}{tab}{b4}"
# print(s)
# print(s2)
# print("-------------")
#
# s = f"{a1}{tab}{a2}{tab}{a3}{tab}{a4}"
# s2 = f"{b1}{tab}{b2}{tab}{b3}{tab}{b4}"
# print(s)
# print(s2)
# print("-------------")
#
# s = f"{a1}\t{a2}\t{a3}\t{a4}"
# s2 = f"{b1}\t{b2}\t{b3}\t{b4}"
# print(s)
# print(s2)
#
# print(s)
# print(s2)
#


# 水仙花数是指一个3 位数，它的每个位上的数字的3次幂之和等于它本身。
# 用for循环优化
# for i in range(100, 1000):
#     a3 = i // 100
#     b3 = (i % 100) // 10
#     c3 = i % 10
#     if a3 ** 3 + b3 ** 3 + c3 ** 3 == i:
#         print(i)
#
# while True:
#     num = int(input('请输入一个正整数\n'))
#     ii4 = 2
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#     if flag:
#         print('这是质数')
#     else:
#         print('这不是质数')


# 水仙花数， 骚气的写法，建议搜索  列表生成式
for num in range(100, 1000):
    if sum([int(i)**3 for i in str(num)]) == num:
        print(num)

# 质数判断
while True:
    num = int(input('请输入一个正整数: '))
    if num == 1:  # 1 特殊处理
        print('1 不是质数')
        continue

    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break # 不是就可以跳出，后面不用再计算
    if flag:
        print('这是质数')
    else:
        print('这不是质数')