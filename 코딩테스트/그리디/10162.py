t = int(input())
a, b, c = 300, 60, 10
a_count,b_count,c_count=0,0,0
if t//a != 0:
    a_count = t//a
    t %= a
if t//b != 0:
    b_count = t//b
    t %= b
if t//c != 0:
    c_count = t//c
    t %= c
if t != 0 :
    print(-1)
else:
    print(a_count, b_count, c_count)