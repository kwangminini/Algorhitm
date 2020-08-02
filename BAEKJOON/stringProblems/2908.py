strList = list(map(str,input().split()))
result=list()
for i in strList:
    result.append(int(i[::-1]))
print(max(result))
