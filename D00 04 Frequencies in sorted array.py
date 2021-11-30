def occ(ls,x):
    n=len(ls)
    start=0
    end=n-1
    first=-1
    while start<=end:
        mid=int((start+end)/2)
        if x==ls[mid]:
            first=mid
            end=mid-1
        elif x<ls[mid]:
            end=mid-1
        else:
            start=mid+1
    if first==-1:
        return -1
    last=-1
    start=0
    end=n-1
    while start<=end:
        mid=int((start+end)/2)
        if x==ls[mid]:
            last=mid
            start=mid+1
        elif x<ls[mid]:
            end=mid-1
        else:
            start=mid+1
    return last-first+1


ls=list(map(int,input().split()))
x=int(input())
print(occ(ls,x))
