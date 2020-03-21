"""
문제 제목 : 숨바꼭질
문제 난이도 : 하
문제 유형 : BFS
------------
특정 위치까지 이동하는 최단 시간을 계산해야 하는 문제
이동 시간이 모두 1초로 동일하므로 간단히 BFS로 해결
큐 구현을 위해 collections 라이브러리의 deque사용
"""

from collections import deque

MAX=100001
n, k = map(int, input().split())
array=[0]*MAX

def bfs():
    q=deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k :
            return array[now_pos]
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            if 0<=next_pos<MAX and not array[next_pos]:
                array[next_pos] = array[now_pos]+1
                q.append(next_pos)

print(bfs())

