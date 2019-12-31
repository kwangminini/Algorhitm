
n=int(input())
inputlist=input().split()
result=[]
for i in range(len(inputlist)):
    result.append(int(inputlist[i]))
result.sort()
print(result[0])