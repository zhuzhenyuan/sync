data = [2]
t = 5
for i in range(1,1001):
    data.append(t + data[i-1])
    t = t+3

# print(data)

while True:
    try:
        print(data[int(input())-1])
        n = int(input())
        for _ in n:
            l = map(int, input().split())
            print(sum(l))

    except Exception as e:
        # print(e)
        break


N