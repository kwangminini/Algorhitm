n=int(input())
inputlist=input().split()
resultstr=""
for i in range(len(inputlist)-1,-1,-1):
    resultstr+=inputlist[i]+" "
print(resultstr)