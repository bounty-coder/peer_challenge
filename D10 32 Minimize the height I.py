# Given an array arr[] denoting heights of N towers and a positive integer K,
# you have to modify the height of each tower either by increasing or decreasing them by K only once.
# Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.
#
#  Note: Assume that height of the tower can be negative.

# Input:
# K = 2, N = 4
# Arr[] = {1, 5, 8, 10}
# Output:
# 5
# Explanation:
# The array can be modified as 
# {3, 3, 6, 8}. The difference between 
# the largest and the smallest is 8-3 = 5.

#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        result=arr[n-1]-arr[0]
        i=1
        while i<n:
            maxi=max(arr[i-1]+k,arr[n-1]-k)
            mini=min(arr[0]+k,arr[i]-k)
            result=min(result,maxi-mini)
            i+=1
        return result
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends