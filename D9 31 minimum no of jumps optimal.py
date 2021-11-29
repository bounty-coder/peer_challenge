# Given an array of N integers arr[] where each element represents
#  the max number of steps that can be made forward from that element.
#  Find the minimum number of jumps to reach the end of the array (starting from the first element).
#  If an element is 0, then you cannot move through that element.

# Note: Return -1 if you can't reach the end of the array.


# Input :
# N = 6
# arr = {1, 4, 3, 2, 6, 7}

# Output: 2 
# Explanation: 
# First we jump from the 1st to 2nd element 
# and then jump to the last element.


# Time complexity O(n)
# Greedy optimal approach


class Solution:
	def minJumps(self, arr, n):
	    #code here
	    maxr=arr[0]
	    jump=1
	    step=arr[0]
	    if n==1:
	        return 0
	    elif arr[0]==0:
	        return -1
	    i=1     
	    while i<n:
	        if i==n-1:
	            return jump
	        maxr=max(maxr,i+arr[i])
	        step-=1
	        if step==0:
	            jump+=1
	            if i>=maxr:
	                return -1
	            step=maxr-i
	        i+=1

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends