import re
str = input()
search = input()

st=[m.start()for m in re.finditer(search,str)]
print(len(st))

