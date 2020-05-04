s = input()
result=''
def reverseStr(str1):
    global result
    result+=str1[::-1]

k=''
for i in range(len(s)):
    if s[i]==' ':
        reverseStr(k)
        k=''
    k+=s[i]

reverseStr(k)
print(result)