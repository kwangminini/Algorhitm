from collections import deque
n,m,v = map(int,input().split())

adj=[[]for _ in range(n+1)]


for i in range(m):
    x, y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

for i in adj:
    i.sort()

def dfs(now):
    print(now, end=" ")
    visited[now]=True
    for nex in adj[now]:
        if visited[nex] == False:
            dfs(nex)

def bfs(now):
    q=deque([now])
    while q:
        now=q.popleft()
        if visited[now]==False:
            visited[now]=True
            print(now,end=" ")
            for nex in adj[now]:
                if not visited[nex]:
                    q.append(nex)
visited=[False]*(n+1)
dfs(v)
print("")

visited=[False] *(n+1)
bfs(v)