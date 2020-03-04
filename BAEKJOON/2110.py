"""
집의 개수 N은 최대 20만개이며, 집의 좌표 X는 최대 1000000000이다
데이터가 굉장히 클 때 탐색문제는 => 이진탐
이진 탐색을 이용하여 O(NlogX)에 문제를 해결 할 수 있음
가장 인접한 두 공유기 사이의 최대 Gap을 이진 탐색으로 찾음

이진탐색 구현법 => 1.재귀적, 2.반복적
"""

n,c=list(map(int, input().split(' ')))
array=[]
for _ in range(n):
    array.append(int(input()))

array.sort()
start=array[1]-array[0]
end=array[-1]-array[0]

result=0
while(start<=end):
    mid=(start+end)//2      #mid는 Gap을 의미
    value=array[0]
    count=1
    for i in range(1,len(array)):
        if array[i]>=value+mid:
            value=array[i]
            count+=1
    if count>=c:        #C개 이상의 공유기를 설치할 수 있는 경우
        start=mid+1
        result=mid
    else:           #C개 이상의 공유기를 설치할 수 없는경우
        end=mid-1
print(result)
