"""
문제 제목 : 암호 만들기
문제 난이도 : 중
문제 유형 : 백트래킹
C개의 문자들이 주어졌을 때, 가능한 L길이의 암호를 모두 찾아야 함
따라서 C개의 문자들 중에서 L개를 선택하는 모든 조합
Python의 조합(combinations)라이브러리를 사용
DFS를 이용하여 조합 함수 구현 가
"""
from itertools import combinations

vowels = ('a','e','i','o','u')
l, c =map(int, input().split())

array=input().split()
array.sort()


for password in combinations(array,l):
    count =0
    for i in password:
        if i in vowels:
            count+=1

    if count>=1 and count <=l-2:
        print(''.join(password))