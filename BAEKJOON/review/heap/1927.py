import heapq
import sys
input = sys.stdin.readline
n=int(input())

heap_data=[]
for _ in range(n):
    data = int(input())
    if data == 0:
        if heap_data:
            print(heapq.heappop(heap_data))
        else:
            print(0)
    else:
        heapq.heappush(heap_data,data)
