"""
sys.stdin.readline() -> input()으로하면 시간초과
데이터의 개수가 최대 100만개
시간복잡도 O(NlogN)의 정렬 알고리즘을 이용해야 함
고급 정렬 알고리즘(병합 정렬, 퀵 정렬, 힙 정렬 등)을 이용하여 문제를 해결할 수 있음
혹은 파이썬의 기본정렬 라이브러리를 이용한다면 문제를 풀 수 있음
메모리가 허용된다면, 되도록 Python3보다는 PyPy3를 선택해서 코드를 제출!!
"""
import sys
n=int(input())
array=[]
for _ in range(n):
    array.append(int(sys.stdin.readline()))
array.sort()
for i in array:
    print(i)