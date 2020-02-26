n=int(input())
array=[]
for i in range(n):
    input_data=input().split()
    array.append((int(input_data[0]),int(input_data[1])))

result=sorted(array,key=lambda x:(x[0],x[1]))
for i in range(len(result)):
    print(result[i][0], result[i][1])