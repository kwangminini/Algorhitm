n=input()
sixteen=[]
sixteenStr=""
def f(n):
    return{
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15}.get(n,n)

def toSixteen(num):
    return{
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F'}.get(num,str(num))
def sixteenJinsu(num):
    sixteen.append(int(int(num)%16))
    #if int(num/16)==0:
     #   sixteen.append(int(int(num)/16))
    if int(num/16)!=0:
        sixteenJinsu(int(int(num)/16))
#sixteenJinsu(f(n))
#sixteen.reverse()


#print(sixteenStr)
def mulSixteen(num):
    global sixteenStr
    sixteenJinsu(num)
    sixteen.reverse()
    for i in range (len(sixteen)):
        sixteenStr+=str(toSixteen(sixteen[i]))
    return sixteenStr
for i in range(1,16):
    print(n+"*"+toSixteen(i)+"="+mulSixteen(int(f(n))*i))
    sixteenStr=""
    sixteen=[]