"""
선반 위에 올려져 있는 트로피들에 대하여 왼쪽에서, 오른쪽에서 봤을 때 보이는 트로피의 수를 각각 구한다.
트로피의 개수 N이 최대 50이므로 단순히 구현
"""
N=int(input())
array=[]
leftCount=1
rightCount=1
for _ in range(N):
    array.append(int(input()))
# print(len(array))
pointer=array[0]
for i in range(len(array)-1):
    if pointer<array[i+1]:
        leftCount+=1
        pointer=array[i+1]

pointer=array[-1]
for i in range(len(array)-1,0,-1):
    if pointer<array[i-1]:
        pointer=array[i-1]
        rightCount+=1

print(leftCount)
print(rightCount)