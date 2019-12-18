
n=input()
k=0
result=0
a=0
mylist=[]


def eightJinsu(num):
 
    if (num/10) >=1:
        a=int(num/10)
        mylist.append(num%10)
        eightJinsu(a)
    else:
       
       mylist.append(num)
   

for i in range (len(n)-1,-1,-1):
    result+=(8**k)*int(n[i])
    k+=1

eightJinsu(result)
b=""
for i in range (len(mylist)-1,-1,-1):
    b+=str(mylist[i])
print(b)


 