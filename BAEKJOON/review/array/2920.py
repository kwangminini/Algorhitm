import sys
input = sys.stdin.readline

test=list(map(int,input().split()))
flag = 1

sortedTest = sorted(test)
reversedTest = sorted(test,reverse=True)

if test == sortedTest:
    print('ascending')
elif test ==reversedTest:
    print('descending')
else:
    print('mixed')