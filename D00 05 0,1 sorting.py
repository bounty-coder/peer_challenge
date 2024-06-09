## Given array of 0 and 1
## sort the array in O(n) time complexity

#TC- O(n)
#SC- O(n)
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



#TC-O(n)
#SC-(1)

def segregate0and1(arr,n):
    zero=0
    one=n-1
    while zero<=one:
        if arr[zero]==1 and arr[one]==0:
            arr[zero],arr[one]=arr[one],arr[zero]
            zero+=1
            one-=1
        elif arr[zero]==1 and arr[one]==1:
            one-=1
        elif arr[zero]==0 and arr[one]==0:
            zero+=1
        else:
            zero+=1
            one-=1
    return arr
