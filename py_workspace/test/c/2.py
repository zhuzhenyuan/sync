import collections
all = []

while True:
    try:
        p, line = input().split()
        key = p.split("\\")[-1]
        all.append((key, line))
    except:
        break


ret = collections.OrderedDict()  # 顺序字典

for one in all:
    if one not in ret:
        ret[one] = 1
    else:
        ret[one] += 1
#
# cc = []
# for one in all:
#     if one in ret:
#         cc.append((one[0], one[1], str(ret[one])))
#         del ret[one]

# sorted(cc, key=lambda one: one[2])

# cc.sort(key=lambda one: one[2], reverse=True)

# for one in cc:
#     a, b, c = one
#     print(' '.join([a[-16:], b, c]))

for key, val in sorted(ret.items(), key=lambda kv:kv[1],reverse = True)[:8]:  # 排序从大到小
    p, line = key
    print(' '.join([p[-16:], line, str(val)]))










