"""
문제 제목 : 카드 정렬하기
문제 난이도 : 하
문제 유형 : 힙, 자료구조, 그리디
가장 크기가 작은 숫자 카드 묶음들을 먼저 합쳤을 때 , 비교 횟수가 가장 적다
"""
import heapq

n=int(input())
heap=[]
result=[]

for _ in range(n):
    heapq.heappush(heap,int(input()))
result2=0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one+two
    result2+=sum_value
    heapq.heappush(heap,sum_value)

print(result2)

