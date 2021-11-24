# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

# Input: arr = [1,3,4,2,2]
# Output: 2


def findDuplicate(arr):
    i=0
    n=len(arr)
    while i<n:
        if arr[i]==i+1:
            i+=1
        else:
            
            if arr[arr[i]-1]==arr[i]:
                return arr[i]
            arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]

arr=[1,3,4,2,2]
print(findDuplicate(arr))