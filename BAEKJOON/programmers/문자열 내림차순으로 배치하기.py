def solution(s):
    answer = ''
    result=[]
    for i in range(len(s)):
        result.append(ord(s[i]))
    result.sort(reverse=True)
    for i in result:
        answer+=chr(i)
    return answer