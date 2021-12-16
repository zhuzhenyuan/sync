def b():
    pass


def a():
    b()
    pass


if __name__ == "__main__":
    a()
    b()

s = '''{}遇到了{}'''
s2 = '''%s遇到了%s'''

print(s.format("1", "2"))
print(s.format("3", "4"))
print(s.format(5, 6))
print(s2 % ("1", "2"))
print(s2 % ("3", "4"))
