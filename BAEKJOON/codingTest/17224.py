n,l,k = map(int, input().split())
result = 0
count = 0
problem = []
for _ in range(n):
    sub1, sub2 = map(int,input().split())
    problem.append((sub1,sub2))

problem.sort(key=lambda x:x[1])
for x,y in problem:
    if count==k:
        print(result)
        exit(0)
    if l>=y:
        result+=140
        count += 1
    elif l>=x and l<y:
        result+=100
        count += 1
print(result)
