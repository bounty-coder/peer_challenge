# Implement the next permutation,
# which rearranges the list of numbers into Lexicographically 
# next greater permutation of list of numbers. 
# If such arrangement is not possible, it must be rearranged to the lowest possible order 
# i.e. sorted in an ascending order. You are given an list of numbers arr[ ] of size N.

# Input: N = 6
# arr = {1, 2, 3, 6, 5, 4}
# Output: {1, 2, 4, 3, 5, 6}
# Explaination: The next permutation of the 
# given array is {1, 2, 4, 3, 5, 6}.

class Solution:
    def nextPermutation(self, n, arr):
        # code here
        i=n-1
        # print("i before loop:",i)
        while i>=0:
            if arr[i]>arr[i-1]:
                break
            i-=1
        # print("i after loop:",i)
        j=i
        while j<n:
            if arr[j]<arr[i-1]:
                break
            j+=1
        arr[i-1],arr[j-1]=arr[j-1],arr[i-1]
        # print(arr[i-1],arr[j-1])
        a=arr[i:n]
        a.reverse()
        ls=arr[:i]+a
        # print(ls)
        return ls
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends