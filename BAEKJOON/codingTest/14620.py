import sys
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for i in range(n)]

ans = 10000
dx, dy = [0,0,0,1,-1],[0,1,-1,0,0]
def ck(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower // n
        y = flower % n
        if x==0 or x==n-1 or y==0 or y==n-1:
            return 10000
        for w in range(5):
            flow.append((x+dx[w],y+dy[w]))
            ret += g[x+dx[w]][y+dy[w]]
    if len(set(flow)) !=15:
        return 10000
    return ret
for i in range(n*n):
    for j in range(n*n):
        for k in range(n*n):
            ans = min(ans, ck([i,j,k]))

print(ans)