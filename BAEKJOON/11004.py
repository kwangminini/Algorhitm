"""
데이터의 개수가 최대 5000000개
시간복잡도 O(NlogN)의 정렬 알고리즘을 이용
시간적 이점을 위하여 PyPy3를 선택하여 코드를 제출
"""
n, k = map(int,input().split())
array=list(map(int, input().split()))
array.sort()
print(array[k-1])