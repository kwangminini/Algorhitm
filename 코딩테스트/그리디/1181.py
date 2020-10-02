n = int(input())
words={}
for _ in range(n):
    word=input()
    if len(word) not in words.keys():
        words[len(word)]={word}
    elif len(word) in words.keys():
        words[len(word)].add(word)
#print(words)
sortWords = sorted(words.items(),key=lambda x:x[0])
#print(sortWords)
for key,item in sortWords:
    sortItem = sorted(item)
    for i in sortItem:
        print(i)