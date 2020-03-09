"""
문서의 길이는 최대 2500이고 단어의 길이는 최대 50
단순히 모든 경우의 수를 계산하여 문제를 해결할 수 있음
시간복잡도 O(NM)의 알고리즘으로 해결할 수 있음
"""
import re
inputStr=input()
searchStr=input()
st=[m.start()for m in re.finditer(searchStr,inputStr)]
print(len(st))