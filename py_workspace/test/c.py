import copy
n = int(input())
k = int(input())
# n=3
# k=3
nums = [i for i in range(1, n+1)]
data = []
def dfs(ll, dst):
    if len(ll) == 0:
        data.append(copy.copy(dst))
        return
    for i in ll:
        dst.append(i)
        tmp = []
        for t in ll:
            if t == i:
                continue
            tmp.append(t)
        dfs(tmp, dst)
        dst.pop()

dfs(nums, [])

sorted(data)
# print(data[k-1])
print(''.join(map(str, data[k-1])))


# print(nums)
# print(nums.pop())
# nums.









1234
1243
1324
1342
1423
1432