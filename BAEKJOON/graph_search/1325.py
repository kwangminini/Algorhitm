"""
문제 제목 : 효율적인 해킹
문제 난이도 : 하
문제 유형 : DFS, BFS
-----------------
모든 정점에 대하여 DFS 및 BFS를 수행
DFS 혹은 BFS를 수행할 때마다 방문하게 되는 노드의 개수를 계산
가장 노드의 개수가 크게 되는 시작 정점을 출력
간선이 많아서 bfs로햇
"""

from collections import deque

n,m = map(int, input().split())
adj=[[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x)

def bfs(v):
    q = deque([v])
    visited = [False] * (n+1)
    visited[v]=True
    count=1
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e]=True
                count+=1
    return count
result =[]
max_value = -1
for i in range(1,n+1):
    c = bfs(i)
    if c>max_value:
        result=[i]
        max_value=c
    elif c == max_value:
        result.append(i)
        max_value=c
for e in result:
    print(e, end=" ")