"""
문제 제목 : 유기농 배추
문제 난이도 : 하
문제 유형 : DFS, BFS

연결 요소의 개수를 세는 문제
모든 정점에 대하여 DFS 및 BFS를 수해앟고, 한 번 방문한 정점은 다시 확인하지 않습니다.
전체적으로 DFS 및 BFS를 수행한 총 횟수를 계산
DFS 및 BFS 응용 문제 중에서 출제 비중이 매우 높은 유형 중 하나
DFS로 문제를 푸는 경우, sys 라이브러리의 setrecursionlimit() 함수 설정을 해줄 필요가 있음
"""

import sys
sys.setrecursionlimit(100000)
def dfs(x,y):
    visited[x][y]=True
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if nx<0 or ny>=m or ny<0 or nx>=n:
            continue
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx,ny)

for _ in range(int(input())):
    m,n,k=map(int,input().split())
    array = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        array[x][y]=1
    result=0
    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i,j)
                result+=1
    print(result)
