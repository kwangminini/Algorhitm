import sys
input = sys.stdin.readline

n = int(input())
online = []
for _ in range(n):
    age, name = input().split()
    online.append([int(age),name])

online.sort(key=lambda x:x[0])
for i in online:
    print(i[0], i[1])