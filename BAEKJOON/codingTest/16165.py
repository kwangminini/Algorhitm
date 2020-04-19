n, m = map(int,input().split())
girls={}
for _ in range(n):
    groupName = input()
    girls[groupName]=[]
    for _ in range(int(input())):
        girls[groupName].append(input())

for _ in range(m):
    search = input()
    quiz = int(input())
    if quiz == 1:
        for key, value in girls.items():
            if search in value:
                print(key)
    if quiz == 0 :
        girl = sorted(girls[search])
        for i in girl:
            print(i)