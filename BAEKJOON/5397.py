testCase=int(input())
for i in range(testCase):
    test=input()
    testList=[]
    point=0
    for j in range(len(test)):
        if test[j]=='<':
            if point > 0:
                point-=1
        elif test[j]=='>':
            point+=1
        elif test[j]=='-':
            if point-1>0 :
                del testList[point-1]
        else :
            testList.insert(point,test[j])
            point+=1
    print(testList)
    
                                                                                           
            