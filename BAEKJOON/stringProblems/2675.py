t = int(input())
for i in range(t):
    a, b = input().split()
    text=""
    for j in range(len(b)):
        text+=int(a)*b[j]
    print(text)