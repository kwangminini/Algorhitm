import sys
input = sys.stdin.readline

n=int(input())
result = input()
bonus=0
resultNum=0
for i in range(len(result)):
    if result[i] == 'O':
        resultNum+=(i+1)+bonus
        if result[i+1] == 'O':
            bonus+=1
        else:
            bonus=0
print(resultNum)