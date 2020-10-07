arr = input().split("-")
s=0
result=[]
for i in arr:
    if len(i.split("+")) > 1:
        k=0
        for j in i.split("+"):
           k+=int(j)
        result.append(k)
    else:
        result.append(int(i))
s+=result[0]
for i in range(1,len(result)):
    s-=result[i]
print(s)
