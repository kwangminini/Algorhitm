testCase=int(input())
a=input().split(" ")
test=int(input())
b=input().split(" ")
aDic={}
bDic={}
for i in range(len(a)):
    aDic[int(a[i])]=a[i]

for i in range(len(b)):
    flag=False
    if int(b[i]) in aDic:
        print("1")
    else:
        print("0")