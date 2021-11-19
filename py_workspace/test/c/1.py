
while True:
    try:
        N, M = list(map(int, input().split()))
        src = list(map(int, input().split()))
        for _ in range(M):
            c, num1, num2 = input().split()
            num1 = int(num1)
            num2 = int(num2)
            if c == "Q":
                a = min(num1,  num2)-1
                b = max(num1,  num2)
                print(max(src[a: b]))
            elif c == "U":
                src[num1-1] = num2
    except:
        break


import sys

sys.stdin = open('1.in', 'r')

# status1 = False
# status2 = False
#
#
# def dfs(s, dist, start, step):
# 	global status1,status2
# 	if status1 or start+step > dist:
# 		return
# 	if s[start+step] == '#':
# 		return
# 	if start+step == dist:
# 		status1 = True
# 		return
# 	dfs(s, dist, start+step, 1)
# 	dfs(s, dist, start+step, 2)


for _ in range(3):

	n, a, b, c, d = list(map(int, input().split()))
	s = input()
	if s.find("##") >= 0:
		print("No")
	else:
		if a < c < b < d:
			print("Yes")
		elif a < b < c < d:
			print("Yes")
		elif a < b < d < c:
			# if s[d-1-1] == '.' and s[d] == '.':
			# 	print("Yes")
			# else:
			# 	if s[b-1-1:d].find('...')
			if s[b - 1 - 1:d + 1].find('...') >= 0:
				print("Yes")
			else:
				print("No")
		else:
			print("No")

# 	if c > d:
# 		# a
# 		# dfs(s, c-1, a-1, 1)
# 		# dfs(s, c-1, a-1, 2)
# 		# dfs(s, d - 1, b - 1, 1)
# 		# dfs(s, d - 1, b - 1, 2)
# 	else:
# 		# # b
# 		# dfs(s, d - 1, b - 1, 1)
# 		# dfs(s, d - 1, b - 1, 2)
# 		# dfs(s, c - 1, a - 1, 1)
# 		# dfs(s, c - 1, a - 1, 2)
# 	print(status1, status2)
# 	if status1 and status2:
# 		print("Yes")
# 	else:
# 		print("No")
# status1 = False
# status2 = False

# a < b
# a < c
# b < d
#
# a < b < c < d
# a < b < d < c
# a < c < b < d


n, a, b, c, d = list(map(int, input().split()))
s = input()
if s[c - 1] == '#' or s[d - 1] == '#' or s[a - 1] == '#' or s[b - 1] == '#' or c == d or s[a-1:c if c> d else d].find("##") >= 0:
	print("No")
else:
	if a < c < b < d or a < b < c < d:
		print("Yes")
	elif a < b < d < c:
		if s[b - 1 - 1:d + 1].find('...') >= 0:
			print("Yes")
		else:
			print("No")
	else:
		print("No")

