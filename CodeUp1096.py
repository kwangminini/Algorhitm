pan=[[0]*19 for i in range(19)]
n=int(input())
for i in range(n):
    num=input().split()
    pan[int(num[0])-1][int(num[1])-1]=1

for i in pan:
    for j in i:
        print(j, end=' ')
    print()