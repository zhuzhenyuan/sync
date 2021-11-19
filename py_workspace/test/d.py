ss = input().split(',')
# ss = [9, 3, 5]
# ss = [1,2,2]
dst = [-1] * len(ss)

num = 0
i = 0
while num < len(ss):
    if dst[i] != -1:
        i += 1
    else:
        one = ss[i]

        have = False
        tmp_idx = i
        j = i + 1
        if j >= len(ss):
            j = 0
        while j != i:
            if dst[j] == -1 and ss[j] > one:
                one = ss[j]
                have = True
                tmp_idx = j
            j += 1
            if j >= len(ss):
                j = 0
        # dst[tmp_idx] = num
        # num += 1
        if have:
            dst[tmp_idx] = num
            num += 1
        else:
            dst[i] = num
            num += 1
        #     pass
        i += 1

    if i >= len(ss):
        i = 0

print(','.join(map(str, dst)))
