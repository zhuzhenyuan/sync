#
# print('sdfs'.isdigit())
# print('1234'.isdigit())
# print('123.0'.isdigit())
# print('123.45'.isdigit())
# print('-123'.isdigit())
# print('23'.isalnum())


# while True:
#     d = input()
#     try:
#         d = int(d)
#         if d % 2 == 0:
#             print("是偶数")
#         else:
#             print("是奇数")
#     except:
#         print("try again")



# while True:
#     d = input()
#     d = eval(d)
#     if type(d) != int:
#         continue
#     if d % 2 == 0:
#         print("是偶数")
#     else:
#         print("是奇数")


# while True:
#     try:
#         d = eval(input())
#     except:
#         print("try again")
#     else:
#         print("是偶数") if d % 2 == 0 else print("是奇数") if type(d) == int else print('try again')
#


# print(id(-5))
# print(id(-5))
# print(id(-6))
# print(id(-6))
# print(id(-7))
# print(id(-7))
# print(id(-256))
# print(id(-256))
# print(id(-256234))
# print(id(-256234))

s = int(2000.0)
print(id(s))
print(id(2000))
print(id(2000.0))
print(s is 2000)

if s == 2000:
    print("**8")


print("**************")

s = int(-5.0)
print(id(s))
print(id(-5))
print(id(-5.0))
print(s is -5)

if s == -5:
    print("**8")

