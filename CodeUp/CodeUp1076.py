letter=input()
#print(ord(letter))
num=97
result=""
while(ord(letter)>=num):
    result+=chr(num)+" "
    num+=1
print(result)