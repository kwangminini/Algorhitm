"""
가장 많이 등장한 문자열을 출력하는 문제와 동일
등장횟수를 계산할 때는 파이썬의 Dictionary 자료형을 이용하면 효과적
dic={}
n=int(input())

for i in range(n):
    str=input()
    if str in dic.keys():
        dic[str]+=1
    else:
        dic[str]=1

result=sorted(dic.items(),key=(lambda x:(x[1])))

print(result[-1][0])
"""
n=int(input())
books={}
for _ in range(n):
    book=input()
    if book in books:
        books[book]+=1
    else:
        books[book]=1
target = max(books.values())
array=[]
for book, num in books.items():
    if num == target:
        array.append(book)
print(sorted(array)[0])