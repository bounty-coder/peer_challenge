# Given an array Arr[] of N integers.
#  Find the contiguous sub-array(containing at least one number) 
# which has the maximum sum and return its sum.

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,n):
        ##Your code here
        i=0
        max_sum=float("-inf")
        cur_sum=0
        while i<n:
            cur_sum+=arr[i]
            if cur_sum>max_sum:
                max_sum=cur_sum
                
            if cur_sum<0:
                cur_sum=0
            i+=1
        return max_sum
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        
        ob=Solution()
        
        print(ob.maxSubArraySum(arr,n))
        
        T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends