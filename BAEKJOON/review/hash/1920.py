n=int(input())
array = list(map(int, input().split()))
result=dict()
for i in array:
    result[i]=True

m=int(input())
search=list(map(int,input().split()))

for i in search:
    if i in result.keys():
        print(1)
    else:
        print(0)
