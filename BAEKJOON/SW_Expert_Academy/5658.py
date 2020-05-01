t = int(input())
boxList=[]
def inputArr(boxStr):
    global n
    leng = n // 4
    for i in range(4):
        boxList.append(boxStr[0:leng])
        boxStr = boxStr[leng:len(boxStr)]


for i in range(t):
    n,k = map(int,input().split())
    boxStr = input()
    for _ in range(n//4):
        inputArr(boxStr)
        boxStr = boxStr[-1]+boxStr[:len(boxStr)-1]
    result = sorted(set(boxList),reverse=True)
    hexa = str(int(("0x"+result[k-1]),16))
    print("#"+str(i+1)+" "+hexa)
    boxList=[]
