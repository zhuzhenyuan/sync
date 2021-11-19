s = """"""

d = s.split('\n')
# print(d)

res = []
tmp = {}
for dd in d:
    if not dd:
        res.append(tmp)
        tmp = {}
    else:
        # if 'https://dev.tencent.com' in dd:
        #     print(dd)
        lines = dd.split(':')
        tmp[lines[0]] = ':'.join(lines[1:])
# print(res)
import json
# print(json.dumps(res,ensure_ascii=False))

result = []
formatkey = '"%s": "%s",'
# formatkey = '%s,%s,'
for line in res:
    one = []
    for k, v in line.items():
        ss = formatkey % (k, v)
        # if len(ss) < 50:
        #     ss += ' ' * (50 - len(ss))
        one.append(ss)
    result.append('{%s},' % ''.join(one))
    # result.append('%s' % ''.join(one))

print('\n'.join(result))

# with open('a.csv', 'w') as f:
#     f.write('\n'.join(result))

