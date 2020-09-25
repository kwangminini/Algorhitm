setNum = input()
roomNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for i in range(len(setNum)):
    if setNum[i] == '6' or setNum[i] == '9':
        roomNum[6]+=1
    else:
        roomNum[int(setNum[i])]+=1
if roomNum[6] % 2 == 0:
    roomNum[6] //= 2
else:
    roomNum[6] = (roomNum[6]//2)+1
print(max(roomNum))