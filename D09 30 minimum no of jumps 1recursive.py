'''
# Given an array of N integers arr[] where each element represents
# the max number of steps that can be made forward from that element. 
# Find the minimum number of jumps to reach the end of the array (starting from the first element).
# If an element is 0, then you cannot move through that element.

# Note: Return -1 if you can't reach the end of the array.
'''

# lets first think about the movement of the array, the first element will be the most far from end and will take maximum number of steps to reach the end.
# If we go recursively, then we will need few variables, just think about them first.

# So, we will need the arr itself, then we will the steps counter also we will need i(the element we are currently in recursion)

#if i>=n-1, that means we already on last element, so we need 0 steps from here.
# We will return 0+1, as returning means we are giving the value to previous element which will take 1 step to reach here.

def minJumps(arr,n):
    #only element, no needed any steps to reach end
    if n==1:
        return 0
    def rec(i,steps,minsteps):
        if i>=n-1:
            return 0
        if arr[i]==0:
            return float("inf")
        for j in range(1,arr[i]+1):
            minsteps = min(minsteps,rec(i+j,steps+1,minsteps))
        return minsteps
    minsteps=float("inf")
    i,steps=0,0
    minsteps=rec(i,steps,minsteps)
    if minsteps==float("inf"):
        return -1
    return minsteps


# lets make this recursion into memoised way. So we will need to implement some kind of cache where it'll store the solution to subproblem and no need to recompute again
def minJumps(arr,n):
    if n==1:
        return 0
    dp=[float("inf") for i in range(n)]
    def rec(i):
        if i>=n-1:
            dp[i]=0
            return dp[i]
        if arr[i]==0:
            dp[i]=float("inf")    #though it is already float("inf"), actually had no need to do this
            return dp[i]
        if dp[i]!=float("inf"):
            return dp[i]
        for j in range(1,arr(i)+1):
            dp[i]=min(dp[i],rec(i+j))
        return dp[i]+1
    dp[0]=rec(i)    #if u see above & think logically, there was no need for "steps" variable, hahaha. Thats ok, this is how we evolve
    if dp[0]==float("inf"):
        return -1
    return dp[0]
