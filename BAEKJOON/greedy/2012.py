"""
문제 제목 : 등수 매기기
문제 난이도 : 하
문제 유형 : 그리디
예상된 등수와 실제 등수의 차이를 최소화
따라서, 예상된 등수를 오름차순으로 정렬
"""
import sys
input = sys.stdin.readline
grade=[]
n=int(input())
for _ in range(n):
    grade.append(int(input()))

grade.sort()
count=0
for i in range(1,n+1):
    count+=abs(i-grade[i-1])

print(count)