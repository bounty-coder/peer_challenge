# Given three arrays sorted in increasing order.
#  Find the elements that are common in all three arrays.

# Pythonic Soln using set 

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        A=set(A)
        B=set(B)
        C=set(C)
        s=[]
        for i in A:
            if i in B:
                s.append(i)
        r=[]
        for i in s:
            if i in C:
                r.append(i)
        z=list(r)
        
        return z
#{ 
#  Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends
