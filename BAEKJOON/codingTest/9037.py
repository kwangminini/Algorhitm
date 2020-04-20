import sys
import copy
sys.setrecursionlimit(100000)
t = int(input())

count=0
def circule(arr):
    global count
    flag = False
    #print(arr)
    for i in range(len(arr)):
        if arr[i]%2 != 0:
            arr[i]+=1
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            flag=True
    if not flag:
        return count
    arr2 = copy.deepcopy(arr)
    #print(arr)
    #print(arr2)
    for i in range(len(arr)):
        if i==0:
            arr[i]+=(arr2[-1]//2)-(arr2[i]//2)
        else:
            arr[i]+=(arr2[i-1]//2)-(arr2[i]//2)
    #print(arr)
    count+=1
    return circule(arr)



for _ in range(t):
    n=int(input())
    array=list(map(int, input().split()))
    print(circule(array))
    count=0