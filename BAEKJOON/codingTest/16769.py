a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
count = 1
while(count<101):
    if count % 3==1:
        if a[1]+b[1] <= b[0]:
            b[1]+=a[1]
            a[1]=0
        else:
            a[1]-=b[0]-b[1]
            b[1]=b[0]
    elif count %3==2:
        if b[1]+c[1] <= c[0]:
            c[1]+=b[1]
            b[1]=0
        else:
            b[1]-=c[0]-c[1]
            c[1]=c[0]
    elif count %3==0:
        if c[1]+a[1] <= a[0]:
            a[1]+=c[1]
            c[1]=0
        else:
            c[1]-=a[0]-a[1]
            a[1]=a[0]
    count+=1

print(a[1])
print(b[1])
print(c[1])