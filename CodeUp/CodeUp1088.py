n=int(input())
mystr=""
for i in range(1,n+1):
    if i%3!=0:
        mystr+=str(i)+" "

print(mystr)