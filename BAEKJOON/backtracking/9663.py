"""
문제 제목 : N - Queen
문제 난이도 : 중
문제 유형 : 백트래킹
N * N 크기의 체스 보드 위에 퀸 N개를 서로 공격할 수 없게 배치
대표적인 백트래킹 문제
DFS를 이용하여 간단히 백드래킹 알고리즘 구현
시간 : DFS > BFS
"""
def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x]-row[i]) == x-i:
            return False

    return True
    # x번째 행에 대하여 처리
def dfs(x):
    global result
    if x == n:
        result+=1
    else:
        for i in range(n):
            row[x]=i
            if check(x):
                dfs(x+1)



n = int(input())
row = [0] * n
result = 0
dfs(0)
print(row)
print(result)