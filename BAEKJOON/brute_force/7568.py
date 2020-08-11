n = int(input())
weight=list()
result = list()
for _ in range(n):
    weight.append(list(map(int,input().split())))
#weightList.sort(key=lambda x:(x[0],x[1]),reverse=True)
weightList=sorted(weight,key=lambda x:(x[0],x[1]),reverse=True)
num=1
count=1
for i in range(len(weightList)-1):
    if (weightList[i][0] > weightList[i+1][0]) and (weightList[i][1] > weightList[i+1][1]):
        result.append((weightList[i],num))
        num = count
        num+=1
    else:
        result.append((weightList[i],num))
    count+=1

result.append((weightList[-1],num))
resultList=list()
for i in range(len(weight)):
    for j in range(len(result)):
        if weight[i] == result[j][0]:
            resultList.append(result[j][1])
for i in resultList:
    print(i, end=" ")