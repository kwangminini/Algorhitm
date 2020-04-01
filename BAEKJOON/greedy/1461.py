"""
문제 제목 : 도서관
문제 난이도 : 중
문제 유형 : 그리드

0보다 큰 책들과 0보다 작은 책들을 나눠서 처리
두개의 우선순위 큐를 이용하여 문제를 효과적으로 해결
마지막 책을 놓을 대는 다시 0으로 돌아올 필요 없으므로, 가장 먼책을 마지막으로 놓는다.


"""

import heapq
import sys

n, m = map(int,input().split())
array = list(map(int,input().split()))
positive = []
negative = []

largest = max(max(array), - min(array))

for i in array:
    if i>0:
        heapq.heappush(positive,-i)
    else:
        heapq.heappush(negative,i)
result =0

while positive:
    result+=heapq.heappop(positive)
    for _ in range(m-1):
        if positive:
            heapq.heappop(positive)

while negative:
    result+=heapq.heappop(negative)
    for _ in range(m-1):
        if negative:
            heapq.heappop(negative)

print(-result*2-largest)