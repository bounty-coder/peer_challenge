# Given two sorted arrays arr1[] of size N and arr2[] of size M. 
# Each array is sorted in non-decreasing order.
# Merge the two arrays into one sorted array in non-decreasing order

# while heapifying the first element is always smallest so always swapping it
# and sorting arr2 in last
# so this soln shows O(nlogn) soln.

import heapq

class Solution:
    def merge(self, arr1, arr2, n, m): 
        # code here
        i=j=0
        while i<n:
            if arr1[i]>arr2[0]:
                arr1[i],arr2[0]=arr2[0],arr1[i]
                heapq.heapify(arr2)
            i+=1
        arr2.sort()
       
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, m=map(int, (input().strip().split()))
        arr1=list(map(int , input().strip().split()))
        arr2=list(map(int , input().strip().split()))
        ob = Solution()
        ans=ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=" ")
        for x in arr2:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends
