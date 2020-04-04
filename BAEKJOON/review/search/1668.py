n = int(input())
array=[]
maxnum=0
for _ in range(n):
    array.append(int(input()))

maxnum=array[0]
leftcount=1
rightcount=1
for i in range(len(array)-1):
    if array[i+1]>maxnum:
        leftcount+=1
        maxnum=array[i+1]

array.reverse()
maxnum=array[0]
for i in range(len(array) - 1):
    if array[i + 1] > maxnum:
        rightcount += 1
        maxnum = array[i + 1]
print(leftcount)
print(rightcount)