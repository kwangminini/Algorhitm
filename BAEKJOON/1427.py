n=input()
mylist=[]
for i in range(len(n)):
    mylist.append(int(n[i]))
mylist.sort(reverse=True)

print(''.join(map(str,mylist)))