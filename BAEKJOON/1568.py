"""
N이 최대 1000000000
K가 반복적으로 증가, 날아가는 새의 마리 수는 빠르게 증가
따라서 문제에서 요구하는 대로 단순히 구현하여 정답처리를 받을 수 있음
"""
num = int(input())
result=0
count=1
while num!=0:
    if count>num:
        count=1
    num-=count
    count+=1
    result+=1
print(result)

