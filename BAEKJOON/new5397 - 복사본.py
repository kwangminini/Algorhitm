
testCase=int(input())
for i in range(testCase):
    test=input()
    leftList=[]
    rightList=[]
    for j in range(len(test)):
        if test[j]=='<':
            if len(leftList)!=0: 
                rightList.append(leftList.pop())
        elif test[j]=='>':
            if len(rightList)!=0:
                leftList.append(rightList.pop())
        elif test[j]=='-':
            if len(leftList)!=0:
                leftList.pop()
        else:
            leftList.append(test[j])

    rightList.reverse()
    print("".join(leftList)+"".join(rightList))

