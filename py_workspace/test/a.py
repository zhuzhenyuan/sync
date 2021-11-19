# nums = []
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     nums.append(num)
#
# for num in nums:
#     count = 0
#     while num >= 3:
#         now = int(num / 3)
#         count += now
#         num = num % 3 + now
#     if num == 2:
#         count += 1
#     print(count)
#
#
#

# while True:
#     try:
#         num = input()
#         # print(num)
#         if num == '':
#             break
#     except:
#         break
#     num = int(num)
#     nums = []
#     for _ in range(num):
#         nums.append(int(input()))
#
#     # print("**")
#     print('\n'.join(map(str,sorted(set(nums)))), end='')

#
# while True:
#     try:
#         s = input()
#         # s = 8
#         num = int(s)
#         if num > 1000:
#             num = 1000
#
#         all = num
#         nums = {i: 1 for i in range(num)}
#         i = 0
#         while all:
#             # print(i)
#             already = 0
#             while True:
#                 if i >= num:
#                     i = i % num
#                 if nums[i]:
#                     already +=1
#                 if already ==3:
#                     break
#                 i = i + 1
#
#             nums[i] = 0
#             all -= 1
#
#
#         print(i)
#         # break
#
#
#     except Exception as e:
#         # print(e)
#         break







#
# while True:
#     try:
#         s = input()
#         # s = "abcqweracb"
#         m = set(s)
#         # print(m)
#         ss = []
#         for i in s:
#             if i in m:
#                 ss.append(i)
#                 m.remove(i)
#         print(''.join(ss))
#         # break
#
#     except Exception as e:
#         # print(e)
#         break



def dfs(x, y):

    pass


while True:
    try:
        ss = []
        for _ in range(9):
            s = input()
            ss.append(s.split())


    except Exception as e:
        break












