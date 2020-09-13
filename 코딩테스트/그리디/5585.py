money = int(input())

moneyArr = [500, 100, 50, 10, 5, 1]
num=0
garage = 1000-money
for i in moneyArr:
    value = garage // i
    num += value
    garage -= value*i

print(num)


