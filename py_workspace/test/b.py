target = input()
source = input()
# target = 'abc'
# source = 'abcaybec'
# target = ''
# source = 'aaaaaaaaaa'

start = -1
if len(target) != 0 and len(target) <= len(source):
    for idx in range(len(source)):
        now = 0
        if target[now] == source[idx]:
            p = source[idx:]
            # if len(target) > len(p):
            #     break
            for y in range(len(p)):
                # if len(p) - y + 1 < len(target) - now + 1:
                #     break
                if target[now] == p[y]:
                    now += 1
                    if now >= len(target):
                        start = idx
                        break

# if not start:
#     print(-1)
# else:
print(start)
# else:
#     print(len(source)-1)

