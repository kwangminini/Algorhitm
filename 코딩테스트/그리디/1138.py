n = int(input())
arr = list(map(int, input().split()))
result=[]
for i in range (len(arr),0,-1):
    result.insert(arr[i-1],i)
for i in result:
    print(i, end=' ')