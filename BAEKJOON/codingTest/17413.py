s = input()
result=''
def reverseStr(str1):
    global result
    result+=str1[::-1]

k=''
flag=True
for i in range(len(s)):
    if s[i] == '<':
        reverseStr(k)
        flag=False
    if not flag:
        result+=s[i]
    if flag:
        if s[i]==' ':
            reverseStr(k)
            result+=' '
            k=''
        else:
            k+=s[i]
    if s[i] == '>':
        flag=True
        k=''

reverseStr(k)
print(result)