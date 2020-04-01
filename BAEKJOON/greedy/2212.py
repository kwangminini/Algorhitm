"""
문제 제목 : 센서
문제 난이도 : 하
문제 유형 : 그리디
"""
import sys
input = sys.stdin.readline

n=int(input())
k=int(input())
dist = list(map(int, input().split()))
dist.sort()
result=[]
for i in range(len(dist)-1):
    result.append(abs(dist[i]-dist[i+1]))
result.sort()
count=0
for i in range(len(result)-(k-1)):
    count+=result[i]

print(count)