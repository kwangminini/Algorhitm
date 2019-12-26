
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

def evenAdd(num):
    if num%2==0:
        return "even"
    elif num%2==1:
        return "odd"

print(evenAdd(a))
print(evenAdd(b))
print(evenAdd(c))