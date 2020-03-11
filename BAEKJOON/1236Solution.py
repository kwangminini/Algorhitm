"""
문제 제목 : 성지키기
문제 난이도 : 하
문제 유형 : 탐색
모든 행과 모든 열에 한명 이상의 경비원이 있어야함
행 기준, 열 기준으로 필요한 경비원의 수를 각각 계산하여 더 큰수를 출력
"""
n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input())

row=[0]*n
column=[0]*m

for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i]=1
            column[j]=1

row_count=0
for i in range(n):
    if row[i]==0:
        row_count+=1

column_count=0
for j in range(m):
    if column[j]==0:
        column_count+=1

print(max(row_count,column_count))