n = int(input())
weightList=list()
for _ in range(n):
    weightList.append(list(map(int,input().split())))
weightList.sort(key=lambda x:(x[0],x[1]),reverse=True)
print(weightList)