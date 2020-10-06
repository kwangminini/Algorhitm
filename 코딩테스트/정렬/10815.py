n = int(input())
numberCard = list(map(int,input().split()))
numberDict = {}
for i in numberCard:
    numberDict[i]=1
m = int(input())
mList = list(map(int,input().split()))
for i in mList:
    if i in numberDict.keys():
        print(1,end=" ")
    else:
        print(0, end=" ")