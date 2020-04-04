import heapq
from collections import deque
n,m,v=map(int,input().split())

array=[[] for _ in range(n+1)]
heap_data=[]
def dfs(now):
    print(now, end=' ')
    visited[now]=True
    for nex in array[now]:
        if not visited[nex]:
            dfs(nex)
def bfs(now):
    q=deque([now])
    while q:
        now=q.popleft()
        if not visited[now]:
            visited[now]=True
            print(now, end=' ')
            for nex in array[now]:
                if not visited[nex]:
                    q.append(nex)


for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    array[y].append(x)

for e in array:
    e.sort()

visited=[False] * (n+1)
dfs(v)
print()
visited=[False] * (n+1)
bfs(v)
