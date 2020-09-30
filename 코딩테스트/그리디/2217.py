n = int(input())
w = []
for _ in range(n):
    w.append(int(input()))
w.sort()
result=0
for i in range(n):
    result = max(result,w[i]*(n-i))
print(result)