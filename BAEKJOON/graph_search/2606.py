"""
문제 제목 : 바이러스
문제 난이도 : 하
문제 유형 : DFS, BFS
DFS 혹은 BFS를 이용하여 방문하게 되는 노드의 개수를 계산
컴퓨터 수가 적으므로, DFS를 이용해 빠르게 문제를 푸는 것이 유리
"""

from collections import deque
n=int(input())
m=int(input())
array=[[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0
for _ in range(m):
    a,b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

def dfs(now_pos):
    global count
    count+=1
    visited[now_pos] = True
    for next_pos in array[now_pos]:
        if visited[next_pos] == False:
            dfs(next_pos)

dfs(1)
print(count-1)