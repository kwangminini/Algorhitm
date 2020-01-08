#완전 탐색
num=list(map(int,input().split()))
n=list(map(int,input().split()))
result=0
maxNum=0
for i in range (num[0]):
    for j in range (i+1,num[0]):
        for z in range (j+1,num[0]):
            result=n[i]+n[j]+n[z]
            if result>maxNum and result<=num[1]:
                maxNum=result
            elif result>num[1]:
                continue

print(maxNum)