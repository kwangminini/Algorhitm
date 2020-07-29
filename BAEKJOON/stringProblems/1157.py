word = input()
word = word.upper()
dict={};
for i in range (len(word)):
    if word[i] in dict:
        dict[word[i]]+=1
    else:
        dict[word[i]]=1
item=sorted(dict.items(), key=lambda x:x[1], reverse=True)
if(len(item)==1):
    print(item[0][0])
for i in range (len(item)-1):
    if item[i][1] == item[i+1][1]:
        print("?")
        break
    else:
        print(item[i][0])
        break