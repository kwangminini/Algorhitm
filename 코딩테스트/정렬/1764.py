n, m = map(int,input().split())
result={}
for _ in range(n+m):
    data = input()
    if data in result.keys():
        result[data]+=1
    else:
        result[data]=1
result2=[]
for key,item in result.items():
    if item == 2:
        result2.append(key)
result2.sort()
print(len(result2))
print('\n'.join(result2))