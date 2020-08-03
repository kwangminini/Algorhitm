testNum = int(input())
result=0
check=[]
def checkGroup(word):
    flag = True
    global result
    for i in range(len(word)-1):
        check.append(word[i])

        if ((word[i+1] in check) and (check[-1] != word[i+1])):
            flag=False

    if flag:
        result+=1


for _ in range(testNum):
    checkGroup(input())
    check=[]
print(result)