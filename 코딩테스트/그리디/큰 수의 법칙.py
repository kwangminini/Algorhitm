n, m, k = map(int,input().split())
numArr = list(map(int,input().split()))
result = 0
count = 0

numArr.sort()
first = numArr[-1]
second = numArr[-2]

for i in range(1,m+1):
    if i%k != 0:
        result+=first
    else:
        result+=second

print(result)


