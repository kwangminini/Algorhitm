"""
문제 제목 : 문제집
문제 난이도 : 중
문제 유형 : 힙, 위상 정렬
전형적인 위상 정렬 문제
위상 정렬은 순서가 정해져 있는 작업을 차례로 수행해야 할 때, 순서를 결정해주는 알고리즘
위상 정렬의 시간 복잡도는 O(V+E)로 문제 해결 가

위상정렬 알고리즘
1) 진입 차수가 0인 정점을 큐에 삽입
2) 큐에서 원소를 꺼내 해당 원소와 간선을 제거
3) 제거 이후에 진입 차수가 0이 된 정점을 큐에 삽입
4) 큐가 빌 때까지 2)-3) 과정을 반복
* 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재
* 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과
"""
import heapq
n,m = map(int,input().split())
array=[[] for i in range(n+1)]
indegree=[0]*(n+1)

heap=[]
result=[]
for _ in range(m):
    x,y=map(int,input().split())
    array[x].append(y) #x와 y연결
    indegree[y]+=1

for i in range(1,n+1): #진입차수가 0인 정점을 큐에 삽입
    if indegree[i]==0:
        heapq.heappush(heap,i)

while heap:
    data=heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y]-=1
        if indegree[y] == 0:
            heapq.heappush(heap,y)

for i in result:
    print(i, end=" ")
