def isAnagram(str1, str2):
    str1List=[]
    str1List.append(str1)
    str2List=[str2]
    sort1list=sorted(str1List[0])
    sort2list=sorted(str2List[0])
    
    for i in range(len(str1)):
        if sort1list[i]!=sort2list[i]:
            return False
    
        
    return True
    
    
    
    

def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
    print(isAnagram('cat', 'cap')) #should return False
    

if __name__ == "__main__":
    main()

