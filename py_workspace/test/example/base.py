def answer1():
    '''
    输入三个整数x,y,z，请把这三个数由小到大输出
    输入: [7,8,6,4,2,1,3,5]
    输出: [1,2,3,4,5,6,7,8]
    '''
    nums = list(map(int, input().split()))
    print(nums)
    print('----')
    # sort1
    s1 = sorted(nums)
    print(s1)
    print(nums)
    print('----')
    # sort2
    nums.sort()
    print(nums)


def answer2():
    '''
    将一个列表的数据复制到另一个列表中
    list1 = [1, 2, 3, 4, 5]
    复制到list2
    '''
    list1 = [1, 2, 3, 4, 5]
    list2 = list1[:]  # 方法一
    print(list2)
    list2 = []  # 方法一
    for t in list1:
        list2.append(t)
    print(list2)


def answer3():
    '''
    输入一行字符，分别统计出其中,英文字母、空格、数字和其它字符的个数
    例如输入： "asd;f;jhSKLDJF@#$KLJ:HDL2342309()4kljkjlsk SEF,;'345WlkJ095"
    输出： char = 33,space = 1,digit = 14,others = 11
    '''
    ss = "asd;f;jhSKLDJF@#$KLJ:HDL2342309()4kljkjlsk SEF,;'345WlkJ095"
    char = 0
    space = 0
    digit = 0
    others = 0
    for c in ss:
        if c == " ":
            space += 1
        elif (c >= "a" and c <= "z") or (c >= "A" and c <= "Z"):
            char += 1
        elif c >= "0" and c <= "9":
            digit += 1
        else:
            others += 1
    print('char = %d,space = %d,digit = %d,others = %d' % (char, space, digit, others))


def answer4(num):
    '''
    利用递归方法求5!
    递归操作
    '''
    if num == 1:
        return num
    return answer4(num-1) + 1


def answer5():
    '''
    统计1-1000的和
    求和
    '''
    print(sum(range(1, 100+1)))


def answer6():
    '''
    统计字符串中元素出现的次数
    输入: "asjakskhkasdfkzasdf"
    输出：[('a', 4), ('s', 4), ('j', 1), ('k', 4), ('h', 1), ('d', 2), ('f', 2), ('z', 1)]
    '''
    ss = "asjakskhkasdfkzasdf"
    ret = {}
    for c in ss:
        if c not in ret:
            ret[c] = 0
        ret[c] += 1
    print(list(ret.items()))


def answer7():
    '''
    复制文本文件
    将a.txt的文件内容，复制到b.txt
    '''
    with open('a.txt', 'r') as f:
        with open('b.txt', 'w') as f2:
            f2.write(f.read())


def answer8():
    '''
    实现字符串数据去重,并按字段序输出
    输入: asdfsdfdsasdfasfsdfadsfsdfdsfaaasdjkasdfaaasfsfza"
    输出: ['a', 'd', 'f', 'j', 'k', 's', 'z']
    '''
    ss = "asdfsdfdsasdfasfsdfadsfsdfdsfaaasdjkasdfaaasfsfza"
    print(sorted(set(ss)))


def answer9():
    '''
    使用MD5或SHA1等算法对用户密码进行加密
    输入: "this a try to md5"
    输出: c52ebf53eda3ee6f3ba000b6b01eeabf
    '''
    import hashlib
    ss = "this a try to md5"
    h1 = hashlib.md5()
    h1.update(ss.encode(encoding='utf-8'))
    print(ss)
    print(h1.hexdigest())


def answer10():
    name = " gouguoQ  "
    # 移除name变量对应值的两边的空格，并输出移除后的内容
    print(name.strip())
    name = name.strip()
    # 判断name变量对应的值是否以"go"开头，并输出结果
    print(name.startswith('go'))
    # 判断name变量对应的值是否以"Q"结尾，并输出结果
    print(name.endswith('Q'))
    # 将name变量对应的值中的"o"，替换为"p"，并输出结果
    print(name.replace('0', 'p'))
    # 将name变量对应的值根据"o"分割，并输出结果
    print(name.split('o'))
    # 请问上一题分割之后得到的值是什么类型
    print(type(name.split('o')))
    # 将name变量对应的值变大写，并输出结果
    print(name.upper())
    # 将name变量对应的值变成小写，并输出结果
    print(name.lower())
    # 请输出name变量对应的值的第二个字符？请输出name变量对应的值的前三个字符.请输出name变量对应值的后2个字符
    print(name[1])
    print(name[:3])
    print(name[-2:])
    # 请输出name变量中的值"Q的索引的位置
    print(name.index('Q'))
    # 获取子序列，仅不包含最后一个字符，如：woaini则获取woain  root则获取roo
    print(name[:-1])
    # 利用下划线将列表的每一个元素拼接成字符串  li = ['gou', 'guo', 'qi'] => "gou_guo_qi"
    print('_'.join(['gou', 'guo', 'qi'] ))

if __name__ == "__main__":
    # answer1()
    # answer2()
    # answer3()
    # print(answer4(5))
    # answer5()
    # answer6()
    # answer7()
    # answer8()
    # answer9()
    answer10()
