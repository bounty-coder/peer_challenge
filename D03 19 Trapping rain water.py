

class Solution:
    def trappingWater(self, arr,n):
        #Code here
        l=[0]*n
        r=[0]*n
        m=0
        for i in range(n):
            m=max(m,arr[i])
            l[i]=m
        m=0
        for i in range(n-1,-1,-1):
            m=max(m,arr[i])
            r[i]=m
        print(l,r)
        i=0
        s=0
        m=min(arr[0],arr[n-1])
        while i<n:
            s+=min(l[i],r[i])-arr[i]
            i+=1
        return s
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        
            
    n=int(input())
    
    arr=[int(x) for x in input().strip().split()]
    obj = Solution()
    print(obj.trappingWater(arr,n))
            
            
         


if __name__ == "__main__":
    main()



# } Driver Code Ends
