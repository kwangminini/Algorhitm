import sys
input = sys.stdin.readline

n = int(input())
str = input()
array = list(map(int, str.split()))
print(max(array)-min(array))