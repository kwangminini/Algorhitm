num=input().split()
k=1
asFlag=False
deFlag=False
asCount=0
deCount=0

for i in range(len(num)-1):
    if int(num[i])+1==int(num[i+1]):
        asFlag=True
        asCount+=1
    elif int(num[i])-1==int(num[i+1]):
        deFlag=True
        deCount+=1
    else:
        asFlag=False
        deFlag=False

if asFlag==True and asCount==7:
    print("ascending")
elif deFlag==True and deCount==7:
    print("descending")
else:
    print("mixed")