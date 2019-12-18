


n=input()
k=0
result=0
a=0
mylist=[]
def f(num):
    if num>9:
        return{
            10:'A',
            11:'B',
            12:'C',
            13:'D',
            14:'E',
            15:'F'
            }.get(num)
    else:
        return num

def eightJinsu(num):
 
    if (num/16) >=1:
        a=int(num/16)
        mylist.append(f(num%16))
        eightJinsu(a)
    else:
       
       mylist.append(f(num))
   

for i in range (len(n)-1,-1,-1):
    result+=(10**k)*int(n[i])
    k+=1

eightJinsu(result)
b=""
for i in range (len(mylist)-1,-1,-1):
    b+=str(mylist[i])
print(b)


 