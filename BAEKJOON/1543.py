"""
inputString=input()
count=0
def search(str,str2){

}
"""
import re
inputStr=input()
searchStr=input()
st=[m.start()for m in re.finditer(searchStr,inputStr)]
print(len(st))