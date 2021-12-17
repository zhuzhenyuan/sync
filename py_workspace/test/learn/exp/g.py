import os
import time

text1 = """
1. aaa\n2. bbbb\n3. cccc
"""
text2 = """
1. aaa\n2. bbbb\n3. cccc
"""
print(text1, end='')
os.system('clear')
print('\r' + text2)

print("aaaaa", end='')

print("\rbbb")

i = 1
text3 = '''
******{i}*******
******{i}*******
******{i}*******
******{i}*******
'''
import os
import time
while True:
    print(text3.format(i=i))
    i += 1
    time.sleep(0.5)
    os.system('clear')
    if i > 100:
        break



# print("")



