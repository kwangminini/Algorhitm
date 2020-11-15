n = int(input())
seatArr = input()

count = seatArr.count('LL')

if count <= 1 :
    print(len(seatArr))
else :
    print(len(seatArr) - count +1)