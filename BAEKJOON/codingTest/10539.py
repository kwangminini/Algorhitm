n = int (input())
array = list(map(int, input().split()))
result = []
result.append(array[0])
for i in range(1,len(array)):
    a = (i+1)*array[i]
    result.append(a-sum(result))

for i in result:
    print(i,end=' ')