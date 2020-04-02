"""
문제 제목 : 컵라면
문제 난이도 : 중
문제 유형 : 그리
정렬 및 우선순위 큐 사용
"""

import heapq
import sys
#input = sys.stdin.readline

n=int(input())
array=[]
heap_data=[]
for _ in range(n):
    a,b=map(int,input().split())
    array.append((a,b))

array.sort(key=lambda x:x[0])

for i in array:
    a=i[0]
    heapq.heappush(heap_data,i[1])
    if a < len(heap_data):
        heapq.heappop(heap_data)

print(sum(heap_data))