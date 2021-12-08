
# 官方的python，是由cython写的，有一个机制，就是启动的时候会为 int 预先创建 -5~256的数字

# 验证
x = 256.0
print('id(256): %d' % id(256))  # 跟浮点数 x 不一样
print('id(x): %d' % id(x))
print('id(256.0): %d' % id(256.0))  # 复用了x创建的数字
print('id(int(256.0)): %d' % id(int(256.0)))  # 跟256一个地址
print(256 is int(x))
print(256 == x)

print("**********")
y = 257.0
print('id(257): %d' % id(257))  # 新创建了数字257
print('id(y): %d' % id(y))
print('id(257.0): %d' % id(257.0) )  # 跟y同一个地址
print('id(int(257.0)): %d' % id(int(257.0)))  # 跟257 不同地址
print(257 is int(y))
print(257 == y)








