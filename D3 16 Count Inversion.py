class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        count=0
        if n>1:
            mid=n//2
            l=arr[:mid]
            r=arr[mid:]
            count+=self.inversionCount(l,len(l))
            count+=self.inversionCount(r,len(r))
            
            i=j=k=0
            
            while i<len(l) and j<len(r):
                if l[i]<r[j]:
                    arr[k]=l[i]
                    i+=1
                else:
                    arr[k]=r[j]
                    count+=len(l)-i
                    j+=1
                k+=1
                    
            while i<len(l):
                arr[k]=l[i]
                i+=1
                k+=1
            
            while j<len(r):
                arr[k]=r[j]
                j+=1
                k+=1
                
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends