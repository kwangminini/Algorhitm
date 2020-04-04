import heapq

heapq_data=[]
result=[]
n=int(input())

for _ in range(n):
    heapq.heappush(heapq_data,int(input()))

while len(heapq_data)!=1:
    data=heapq.heappop(heapq_data)+heapq.heappop(heapq_data)
    heapq.heappush(heapq_data,data)
    result.append(data)

count=0
for i in result:
    count+=i
print(count)