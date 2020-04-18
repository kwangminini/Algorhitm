import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
alphabet={'A' : 3, 'B' : 2, 'C' : 1, 'D' : 2, 'E' : 4, 'F' : 3, 'G' : 1, 'H' : 3,
          'I' : 1, 'J' : 1, 'K' : 3, 'L' : 1, 'M' : 3, 'N' : 2, 'O' : 1, 'P' : 2,
          'Q' : 2, 'R' : 2, 'S' : 1, 'T ': 2, 'U' : 1, 'V' : 1, 'W' : 1, 'X' : 2, 'Y' : 2, 'Z' : 1}
n, m = map(int , input().split())
a, b = list(map(str,input().split()))
resultStr=""
for i in range(min(n,m)):
    resultStr+=a[i]
    resultStr+=b[i]


if max(n,m) == len(a):
    resultStr+=a[min(n,m):max(n,m)]
elif max(n,m) == len(b):
    resultStr+=b[min(n,m):max(n,m)]

resultArr=[]
for i in range(len(resultStr)):
    resultArr.append(alphabet[resultStr[i]])
def love(arr):
    if len(arr) == 2:
        if(arr[0] == '0'):
            arr.remove('0')
       # print(''.join(arr)+'%')
        return (print(''.join(arr)+'%'))
    arry=[]
    for i in range(len(arr)-1):
        arry.append(str(int(arr[i])+int(arr[i+1]))[-1])

    love(arry)
love(resultArr)