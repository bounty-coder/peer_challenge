## Given array of 0 and 1
## sort the array in O(n) time complexity


def binfun(arr,n):
    ls=[]
    for i in range(n):
        if arr[i]==0:
            ls.insert(0,0)
        elif arr[i]==1:
            ls.append(1)
    
    return ls


arr=list(map(int,input().split()))
n=len(arr)
print(binfun(arr,n))
