n=int(input())
num=input().split()
result=[0]*23
for i in num:
    result[int(i)-1]+=1
resultstr=""
for i in result:
    resultstr+=str(i)+" "
print(resultstr)
