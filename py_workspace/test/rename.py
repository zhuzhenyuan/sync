import os
# path = 'F:\\u\\黄梅戏\\rmvb'
# path = 'F:\\u\\黄梅戏\\mp4'
# path = 'F:\\u\\黄梅戏\\avi'
# path = 'F:\\u\\京剧视频\\空中剧院'
# path = 'F:\\u\\京剧视频\\京剧'
path = 'F:\\u\\越剧2'
print(path)

print(sorted(os.listdir(path)))
start = 3

def get_num(num):
    if num<10:
        return '00'+str(num)
    elif num <100:
        return '0'+str(num)
    elif num <1000:
        return str(num)
    else:
        raise Exception("num error")

for name in sorted(os.listdir(path)):
    # old_name = ' '.join(name.split(' ')[1:])
    # new_name = name[4:]
    new_name = name
    old = os.path.join(path, name)
    # new = os.path.join(path, str(start)+' '+old_name)
    new = os.path.join(path, get_num(start)+' '+new_name)
    start += 1
    print(old)
    print(new)
    os.rename(old, new)



# os.rename('g:\\py_workspace\\test\\a', 'g:\\py_workspace\\test\\b')

