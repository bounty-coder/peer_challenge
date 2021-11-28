# Given an array of N integers arr[] where each element represents
# the max number of steps that can be made forward from that element. 
# Find the minimum number of jumps to reach the end of the array (starting from the first element).
# If an element is 0, then you cannot move through that element.

# Note: Return -1 if you can't reach the end of the array.

# Following program shows dynamic programming implementation
# Time complexity O(n^2)

class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if n==0:
	        return 0
	    elif arr[0]==0 and n>1:
	        return -1
	    elif arr[0]==0:
	        return 0
	    i=1
	    jumps=[float('inf')]*n
	    jumps[0]=0
	    while i<n:
	        j=0
	        while j<i:
	            if i<=j+arr[j] and jumps[j]!=float('inf'):
	                jumps[i]=min(jumps[i],jumps[j]+1)
	                break
	            j+=1
	        i+=1
	    for i in range(n):
	        if jumps[i]==float('inf'):
	            jumps[i]=-1
	    return jumps[n-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3


Arr = [int(x) for x in input().split()]
n=len(Arr)
ob = Solution()
ans = ob.minJumps(Arr,n)
print(ans)
# } Driver Code Ends