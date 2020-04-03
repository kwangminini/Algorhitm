import sys
input = sys.stdin.readline

n,m=map(int,input().split())
test = list(map(int,input().split()))

test.sort()
result = 0

for i in range(len(test)-2):
    #count=test[i]
    for j in range(i+1,len(test)-1):
        #count+=test[j]
        for z in range(j+1,len(test)):
            count=0
            count+=test[i]+test[j]+test[z]
            if count<=m:
                result = max(result,count)

print(result)