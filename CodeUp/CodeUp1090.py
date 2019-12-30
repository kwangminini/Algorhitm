num=input().split()
a=int(num[0])
d=int(num[1])
n=int(num[2])
mylist=[]
while len(mylist)<n:
    mylist.append(a)
    a*=d
print(mylist[-1])
