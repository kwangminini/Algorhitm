import sys
input = sys.stdin.readline

t=int(input())

for _ in range(t):
    leftStack = []
    rightStack = []
    pwd = str(input())
    for i in range(len(pwd)):
        if pwd[i] == '<':
            if len(leftStack) !=0:
                rightStack.append(leftStack.pop())
        elif pwd[i] == '>':
            if len(rightStack) != 0:
                leftStack.append(rightStack.pop())
        elif pwd[i] == '-':
            if len(leftStack) !=0:
                leftStack.pop()
        else:
            leftStack.append(pwd[i])
    leftStack.extend(reversed(rightStack))
    print(''.join(leftStack))
