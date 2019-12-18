

n=input()
k=0
result=0
a=0
mylist=[]
def f(num):
   
    return{
            'a':10,
            'b':11,
            'c':12,
            'd':13,
            'e':14,
            'f':15
            }.get(num,num)


def eightJinsu(num):
 
    if (num/8) >=1:
        a=int(num/8)
        mylist.append(num%8)
        eightJinsu(a)
    else:
       
       mylist.append(num)
   

for i in range (len(n)-1,-1,-1):
    result+=(16**k)*int(f(n[i]))
    k+=1

eightJinsu(result)
b=""
for i in range (len(mylist)-1,-1,-1):
    b+=str(mylist[i])
print(b)


 