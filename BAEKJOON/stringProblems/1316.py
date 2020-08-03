testNum = int(input())
result=0
check=[]
def checkGroup(word):
    flag=True
    global result
    for i in range(len(word)):
        check.append(word[i])
        if (word[i] in check) and (check[-1] != word[i]):
            flag=False
    if flag:
        result+=1


for _ in range(testNum):
    checkGroup(input())
    print(result)
    check=[]