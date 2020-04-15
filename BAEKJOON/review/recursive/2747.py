n=int(input())

array=[0,1]

def fibonachi(count,num):
    if count <= num:
        array.append(array[count-1]+array[count-2])
        fibonachi(count+1,num)
    else:
        print(array[-1])
fibonachi(2,n)
