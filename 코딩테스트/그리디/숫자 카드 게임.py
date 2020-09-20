n, m = map(int,input().split())
arr = [list(map(int, input().split()))for _ in range(n)]

result=0
for i in arr:
    if result < min(i):
        result = min(i)

print(result)