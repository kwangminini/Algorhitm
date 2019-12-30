n=int(input())
mystr=""
for i in range(1,n+1):
    if i==3 or i==6 or i==9:
        mystr+='X'+" "
    else:
        mystr+=str(i)+" "
print(mystr)