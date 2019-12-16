n=str(input())
intList=[]
MAX_INT=10000
for i in range (len(n)):
    print("["+str(int(n[i])*MAX_INT)+"]")
    MAX_INT = int(MAX_INT/10)

    
