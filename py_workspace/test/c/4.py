# while True:
#     try:
#         print(len(input().split()[-1]))
#     except:
#         break
#
#
#
#
# while True:
#     try:
#         # s = input()
#         # c = input()
#         # s, c, = input(), input()
#         print(input().lower().count(input().lower()))
#     except:
#         break
#
#
# while True:
#     try:
#         s = input()
#         # s = "0.8"
#         a, b = s.split('.')
#         if b[0] >= '5':
#             print(int(a)+1)
#         else:
#             print(int(a))
#     except:
#         break




from collections import Counter, deque, OrderedDict, defaultdict
import math

# while True:
#     try:
#         m = Counter()
#         n = input()
#         for _ in range(int(n)):
#             key, val = input().split()
#             key, val = int(key), int(val)
#             m[key] = m[key] + val
#         for key in sorted(m):
#             print(key, m[key])
#     except:
#         break
# from collections import Counter, deque, OrderedDict, defaultdict
# while True:
#     try:
#         s = input()
#         # s = '9876673'
#         l = OrderedDict()
#         for c in reversed(s):
#             l[c] = 0
#         print(''.join(l.keys()))
#     except:
#         break
#
# while True:
#     try:
#         s = input()
#         print(len(set(s)))
#     except:
#         break
#
# while True:
#     try:
#         s = input()
#         print(''.join(reversed(s)))
#     except:
#         break
#
#
# while True:
#     try:
#         s = input().split()
#         print(' '.join(reversed(s)))
#     except:
#         break
#
#
# while True:
#     try:
#         s = int(input())
#         l = []
#         for _ in range(s):
#             l.append(input())
#         print('\n'.join(sorted(l)))
#         # print(' '.join(reversed(s)))
#     except:
#         break
#
#
# while True:
#     try:
#         s = int(input())
#         print(str(bin(s))[2:].count('1'))
#     except:
#         break
#
#
#
#
# while True:
#     try:
#         s = int(input())
#         l = list(map(int, input().split()))
#         t = int(input())
#         if t == 0:
#             print(' '.join(map(str,sorted(l))))
#         else:
#             print(' '.join(map(str,sorted(l, reverse=True))))
#
#         # print(' '.join(reversed(s)))
#     except Exception as e:
#         print(e)
#         break
#

# while True:
#     try:
#         s = int(input())
#         if s == 1 or s ==2:
#             print(1)
#         else:
#             a, b = 1,1
#
#             for _ in range(s-2):
#                 a,b = b, a+b
#             print(b)
#
#     except:
#         break

# '%6f' % (1.0/(2**9))

# a = int(input())
# print('%.6f' % (3.875*a-a))
# print('%.6f' % (0.03125*a))

#
# def check(s):
#     for num in map(int, s.split('.')):
#         if num <0 or num > 255:
#             return False
#     return True
#
# def check2(s):
#     ss = ""
#     for num in map(int, s.split('.')):
#         ss += str(bin(num))[2:].zfill(8)
#     # print(ss)
#     for c in ss[ss.find('0'):]:
#         if c == '1':
#             return False
#     return True
#
# while True:
#     try:
#         # n, ip1, ip2 = input(), input(), input()
#         n = '255.255.255.0'
#         ip1 = '192.168.0.254'
#         ip2 = '192.168.0.1'
#         if all(map(check, [n, ip1, ip2])) and check2(n):
#             a = []
#             b = []
#             for p1, p2, m in zip(ip1.split('.'), ip2.split('.'), n.split('.')):
#                 p1, p2, m = int(p1), int(p2), int(m)
#                 a.append(p1&m)
#                 b.append(p2&m)
#
#             if a == b:
#                 print(0)
#             else:
#                 print(2)
#         else:
#             print(1)
#
#     except Exception as e:
#         print(e)
#         break

# s = input()
# s = '1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\]['
# import sys
# s = sys.stdin.readline()

# while True:
#     try:
#         s = input()
#         r = [0, 0, 0, 0]
#         for c in s:
#             if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
#                 r[0] += 1
#             elif c == ' ':
#                 r[1] += 1
#             elif '0' <= c <= '9':
#                 r[2] += 1
#
#             else:
#                 r[3] += 1
#         print('\n'.join(map(str, r)))
#
#     except:
#         break

while True:
    try:
        input()
        w = map(int, input().split())
        n = list(map(int, input().split()))

        # w = list(map(int, '69 54 119 85 103 53 155 170'.split()))
        # n = list(map(int, '6 6 3 7 6 2 2 4'.split()))
        l = []
        for idx, i in enumerate(w):
            l.extend([i] * n[idx])

        # l = list(set(l))
        # print(l)
        r = [0]
        for one in l:
            t = []
            for i in r:
                t.append(i+one)
            r.extend(t)
            # print(len(r))
            r = list(set(r))

        # print((all))
        print(len(set(r)))
        break
    except:
        break



# =======
n, m = 0, 0
d = []
# n, m = 4, 6
# d = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0],
# ]

# d = [
# [0, 0, 1, 1, 1, 1],
# [1, 0, 1, 0, 0, 0],
# [1, 0, 0, 0, 1, 0],
# [1, 1, 1, 1, 0, 0],
# ]

step = []
ret = []


def dfs(d, x, y):
    global ret

    if x >= n or y >= m or x < 0 or y < 0:
        return
    if ret:
        return

    if not ret and x == n - 1 and y == m - 1:
        step.append((n - 1, m - 1))
        ret = step
        return

    if d[x][y] == 0:
        step.append((x, y))
        d[x][y] = 2
        # print(step)
        dfs(d, x + 1, y)
        dfs(d, x, y + 1)
        dfs(d, x - 1, y)
        dfs(d, x, y - 1)
        if ret:
            return
        step.pop()
        d[x][y] = 0


while True:
    try:
        ret = []
        n, m = list(map(int, input().split()))
        d = []
        for _ in range(n):
            d.append(list(map(int, input().split())))
        step = []
        dfs(d, 0, 0)
        print('\n'.join(map(lambda a: str(a).replace(' ', ''), ret)))

    except Exception as e:
        print(e)
        break



try:
    s = input()
    # s = '3+2*{1+2*[-4/(8-6)+7]}'
    s = s.replace('[', '(').replace(']', ')').replace('{', '(').replace('}', ')')
    # print(s)
    print(int(eval(s)))
except:
    print(s)



while True:
    try:
        input()
        d = input().split()
        idx = int(input())
        if idx > len(d) or idx <= 0:
            print(0)
        else:
            print(d[-idx])

        pass
    except:
        break


while True:
    try:
        n = int(input())
        if n == 1or n==2:
            print(-1)
        elif n %4 == 1 or n %4==3:
            print(2)
        elif n%4==0:
            print(3)
        elif n%4==2:
            print(4)

        pass
    except:
        break

while True:
    try:
        s = int(input())
        all = set()
        for i in range(1, s+1):
            if i%7==0 or '7'in str(i):
                all.add(i)
        print(len(all))
    except:
        break


while True:
    try:
        pass
        print(int(input())+int(input()))
    except:
        break


while True:
    try:
        n, k = list(map(int, input().split()))
        print(' '.join(map(str, sorted(list(map(int, input().split())))[:k])))
    except:
        break


from collections import Counter
while True:
    try:
        s = input()
        d = Counter(s)
        for c in s:
            if d[c] == 1:
                print(c)
                break
        else:
            print(-1)
    except:
        break

from collections import Counter
while True:
    try:
        s = map(int, input().split('.'))
        for c in s:
            if c <0 or c>255:
                print('NO')
                break
        else:
            print('YES')
    except:
        break

def dfs(n, m):
    if n<0 or m <0:
        return 0
    if n==0 or m==0:
        return 1
    else:
        return dfs(n - 1, m) + dfs(n, m - 1)

while True:
    try:
        a, b = map(int, input().split())
        # a, b = 2,2
        g = dfs(a, b)
        print(g)
    except:
        break


while True:
    try:
        s = input()
        # s = 'abcd12345ed125ss123058789'
        s += 'a'
        start = end = -1
        lenth= 0
        ss = []
        for idx, c in enumerate(s):
            if '0'<=c<='9':
                if start != -1:
                    continue
                start=idx
            else:
                if start == -1:
                    continue
                end =idx
                if end-start > lenth:
                    lenth = end-start
                    ss = [s[start:end]]
                elif end-start == lenth:
                    ss.append(s[start:end])
                start = -1
                end = -1
                # print(ss)
        # ss.append(str(lenth))
        print(''.join(ss)+','+str(lenth))
        # break
    except:
        break


while True:
    try:
        s = input()
        # s = 'abcd12345ed125ss123058789'
        s += 'a'
        start = end = -1
        lenth= 0
        ss = []
        for idx, c in enumerate(s):
            if '0'<=c<='9':
                if start != -1:
                    continue
                start=idx
            else:
                if start == -1:
                    continue
                end =idx
                if end-start > lenth:
                    lenth = end-start
                    ss = [s[start:end]]
                elif end-start == lenth:
                    ss.append(s[start:end])
                start = -1
                end = -1
                # print(ss)
        # ss.append(str(lenth))
        print(''.join(ss)+','+str(lenth))
        # break
    except:
        break


a= []
b= []
status = 0
def dfs(l):
    global a,b,status
    if status:
        return
    if len(l) == 0:
        if sum(a) == sum(b):
            status = 1
        return
    num = l.pop()
    a.append(num)
    dfs(l)
    if status:
        return
    a.pop()
    b.append(num)
    dfs(l)
    if status:
        return
    b.pop()
    l.append(num)

while True:
    try:
        input()
        s = map(int, input().split())
        # s = list(map(int, '3 8 8 5 14'.split()))
        status = 0
        a = list(filter(lambda i: i % 5 == 0, s))
        b = list(filter(lambda i: i % 3 == 0, s))
        all = list(filter(lambda i: i % 3 != 0 and i % 5 != 0, s))
        # print(a)
        # print(b)
        # print(all)
        dfs(all)
        if status:
            print('true')
        else:
            print('false')
        # break
    except Exception as e:
        # print(e)
        break

from collections import OrderedDict,Counter

while True:
    try:
        input()
        # pep = OrderedDict([(i, 1) for i in input().split()])
        pep = input().split()
        input()
        coutn = Counter(input().split())
        for one in pep:
            print(one + ' : '+str(coutn[one]))
            del coutn[one]
        print('Invalid : ' + str(len(coutn.values())))

    except Exception as e:
        # print(e)
        break










