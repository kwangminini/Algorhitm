
num=input().split()
a=int(num[0])
m=int(num[1])
d=int(num[2])
n=int(num[3])
resultList=[]
result=0
result+=a*m+d
resultList.append(a)

for i in range (n-1):
    resultList.append(result)
    result=(result*m)+d
  

print(resultList[-1])