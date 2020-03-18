"""
문제 제목 : DFS와 BFS
문제 난이도 : 하
문제 유형 : DFS, BFS
-----------------
기본적인 형태의 그래프를 단순히 DFS와 BFS로 탐색
정점번호가 작은것을 먼저 방문
모든 노드와 간선을 차례로 조회하여 O(N+M)
국내 코딩테스트에서 가장 중요
큐(Queue)구현을 위해 collections라이브러리의 deque를 사
"""
from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)

def bfs(v):
    q=deque([v])
    while q:
        v=q.popleft()
        if not(visited[v]):
            visited[v]=True
            print(v,end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)

n,m,v = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    x, y=map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)

