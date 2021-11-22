# Given an unsorted array and a number n, 
# find if there exists a pair of elements in the array whose difference is n. 

# following soln has Time complexity O(nlogn) 

def findpair(arr,n):
    arr.sort()
    i=0
    while i<len(arr)-1:
        start=i+1
        end=len(arr)-1
        while start<=end:
            mid=(start+end)//2
            if arr[mid]==arr[i]+n:
                return (arr[i],arr[mid])
            elif arr[mid]<arr[i]+n:
                start=mid+1
            elif arr[mid]>arr[i]+n:
                end=mid-1
        i+=1
    return -1




arr = [1, 8, 30, 40, 100]
n = 60
print(findpair(arr, n))