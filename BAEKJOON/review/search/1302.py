n=int(input())

books=dict()
for _ in range(n):
    book = input()
    if book in books.keys():
        books[book]+=1
    else:
        books[book]=1

target = max(books.values())
array = []
for book,num in books.items():
    if num == target:
        array.append(book)
print(sorted(array)[0])