
num=int(input())
result=0
for i in range(num):
    if result>=num:
        print(i-1)
        break
    else:
        result+=i