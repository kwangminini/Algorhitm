n = int(input())
      #L, R, U, D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
moveType = ['L','R','U','D']
x,y=1,1
plans = input().split()
for i in plans:
    for j in range(len(moveType)):
        if i == moveType[j]:
            nx = x+dx[j]
            ny = y+dy[j]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x,y)
