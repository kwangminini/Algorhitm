
num=input().split()
a=int(num[0])
b=int(num[1])
c=int(num[2])
day=1
while (day%a!=0 or day%b!=0 or day%c!=0):
    day+=1

print(day)