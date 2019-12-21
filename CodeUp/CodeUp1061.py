a,b=input().split()
a=int(a)
b=int(b)
bit=[]
bitstr=""
def bitFunction(a):
    global bitstr
    if a==1:
        return str(1)
    if a==0:
        return str(0)
    if ((int(a/2))==1):
        bitstr+=str(a%2)
        bitstr+=str(int(a/2))
        #bit.append(a%2)
        #bit.append(int(a/2))
        return bitstr[::-1]
    else:
        bitstr+=str(a%2)
        
        #bit.append(a%2)
        bitFunction(int(a/2))
        return bitstr[::-1]

resulta=""
resulta+=(bitFunction(a))
bitstr=""

resultb=""
resultb+=(bitFunction(b))
bitstr=""

if len(resulta)>len(resultb):
    resultb=resultb.zfill((len(resulta)-len(resultb))+len(resultb))
    
else:
    resulta=resulta.zfill(len(resultb)-len(resulta)+len(resulta))
result=""

for i in range(len(resulta)):
   
    if (resulta[i]=="1" or resultb[i]=="1"):
        result+="1"
    else:
        result+="0"
resultNumber=0

j=0
for i in range (len(result)-1,-1,-1):
    resultNumber+=(int(result[i])*(2**j))
    j+=1
print(resultNumber)