from collections import deque

n,k = map(int,input().split())
MAX=100001
array = [0]*MAX

def bfs(now):
    q=deque([now])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        else:
            for next_pos in (now_pos-1,now_pos+1,2*now_pos):
                if 0<=next_pos<MAX and not array[next_pos]:
                    array[next_pos] = array[now_pos]+1
                    q.append(next_pos)

print(bfs(n))
