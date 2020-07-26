import re
alpha = input()
result=[]
for i in range (97,123,1):
    result.append(alpha.find(chr(i)))

for i in result:
    print(i,end=" ")