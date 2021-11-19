
class A(object):
    def __init__(self):
        self.t = "1"
    def run(self):
        print(self.t2)
        print("************************************")


class B(object):
    def __init__(self):
        self.t2 = "2"
    def run(self):
        print(self.t)
        print("##################################")

class C(object):
    pass

def run(self):
    print(self.t)
    print("##################################2222222")

a = A()
b = B()

A.t = "33333333"
c = B.run.__get__(A)
print(c)
c()
# d = c()
# d.run()

c = B.run.__get__(a, A)
print(c)
c = B.run.__get__(None, A)
print(c)
print(B.run)
run.__get__(a)()

print(b.run.__func__)
print(b.run.__self__)
# B.run.__get__(b, Cls)()
#
# B.run(a)
# print(A)
# print(A.run)
#
# print(dir(A.run))
# print('__get__' in dir(A.run))
print('__get__' in dir(b.run))
# print('__set__' in dir(A.run))
# print('__delete__' in dir(A.run))
# print(A.run)
























