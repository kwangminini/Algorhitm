import sys
input = sys.stdin.readline

n=int(input())
array=[]
result=[]
data=[]
count=1

for _ in range(n):
    num=int(input())
    while count<=num:
        array.append(count)
        result.append("+")
        count+=1
    if num==array[-1]:
        result.append("-")
        array.pop()
    else:
        print("NO")
        exit(0)

print('\n'.join(result))