
n=input().split()
a=int(n[0])
b=int(n[1])
c=int(n[2])
count=0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(str(i)+" "+str(j)+" "+str(k))
            count+=1
print(count)