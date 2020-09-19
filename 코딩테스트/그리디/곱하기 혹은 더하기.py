s = str(input())
result=0
def col(one,two):
    global result
    intOne = int(one)
    intTwo = int(two)
    if (int(one) == 1 or int(one) == 0) or (int(two) == 1 or int(two) == 0):
        result = intOne+intTwo
    else:
        result = intOne * intTwo
    #print(one, " ", two, " ", result)
col(s[0],s[1])
for i in range(2,len(s)):
    col(result,s[i])

print(result)

