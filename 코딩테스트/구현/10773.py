k=int(input())
num=[]
for _ in range(k):
    money = int(input())
    if money == 0:
        num.pop(-1)
    else:
        num.append(money)

print(sum(num))