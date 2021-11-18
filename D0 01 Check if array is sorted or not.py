# Check whether an array is sorted or not

def incr(ls):
    i=0
    while i<len(ls)-1:
        if ls[i]>ls[i+1]:
            return False
        i+=1
    return True

def decr(ls):
    i=0
    while i<len(ls)-1:
        if ls[i]<ls[i+1]:
            return False
        i+=1
    return True

ls= list(map(int,input().split()))
if incr(ls) or decr(ls) is True:
    print("Sorted")
else:
    print("Not sorted")