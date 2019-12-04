def isParenthesisValid(st):
    stack=[]
    pDic={'}':'{',')':'(','>':'<',']':'['}
    pOpens={'(','{','<','['}
    
    for ch in st:
        if ch in pOpens:
            stack.append(ch)
            
        else:
            if (len(stack)!=0) and stack[-1] == pDic[ch]:
                stack.pop()
            else:
                return False
                
    if len(stack)!=0:
        return False
    return True
def main():
    examples = ["({()})", "[]<>{}", ")(" "<]", "<(>)"]
    for example in examples:
        print(example, isParenthesisValid(example))

    
if __name__ == "__main__":
    main()