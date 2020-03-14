"""
문제 제목 : 최소 힙
문제 난이도 : 하
문제 유형 : 힙, 자료구조
최소 힙의 기본적인 기능을 구현
heapq 라이브러리를 이용하면 간단히 힙 구현 가능
배열로 하니 시간초과 -> 최소 힙
"""
import heapq
n=int(input())
heap=[]
result=[]
for _ in range(n):
    data = int(input())
    if data == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)

    else:
        heapq.heappush(heap,data)
for data in result:
    print(data)