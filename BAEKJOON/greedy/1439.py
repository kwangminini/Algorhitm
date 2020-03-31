"""
문제 제목 : 뒤집기
난이도 : 하
문제 유형 : 그리디

문자열 S의 길이는 100만 이하이므로, 시간 복잡도는 O(N)에 해결
경우의 수 2
1. 모두 0으로 만드는 경우
2. 모두 1로 만드는 경
"""
data =input()
count0 = 0 #전부 0으로 바꾸는 경우
count1 = 0 #w전부 1로 바꾸는 경우

if data[0] =='1':
    count0+=1
else:
    count1+=1

for i in range(len(data)-1):
    if data[i] !=data[i+1]:
        #다음 수에서 1로 바뀌는 경우
        if data[i+1] == '1':
            count0+=1
        else:
            count1+=1

print(min(count0,count1))