dial = {3:['A','B','C'], 4:['D','E','F'], 5:['G','H','I'], 6:['J','K','L'], 7:['M','N','O'],8:['P','Q','R','S'],
        9:['T','U','V'], 10:['W','X','Y','Z']}
listStr = input()
result=0
for i in range(len(listStr)):
    for key,value in dial.items():
        if listStr[i] in value:
            result+=key

print(result)