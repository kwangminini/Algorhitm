n=int(input())
array=[0,1]
def fibonachi(a, b, count):
    array.append(a+b)
    if count!=0:
        return fibonachi(b,a+b,count-1)
    else:
        return

fibonachi(0,1,43)
print(array[n])


