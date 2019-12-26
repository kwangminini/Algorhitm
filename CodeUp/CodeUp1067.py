n=input()
n=int(n)

def minusOrPlus(n):
    if(n<0):
        return "minus"
    else:
        return "plus"

def oddOrEven(n):
    if(n%2==0):
        return "even"
    else:
        return "odd"

print(minusOrPlus(n))
print(oddOrEven(n))