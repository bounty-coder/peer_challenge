# Complete the function rotateby90() which takes the matrix as input parameter and
#  rotates it by 90 degrees in anti-clockwise direction without using any extra space.
#  You have to modify the input matrix in-place. 

# Expected Time Complexity: O(N2)
# Expected Auxiliary Space: O(1)



class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,a, n): 
        # code here
        i=0
        while i<int(n//2):
            j=i
            while j<int(n-1-i):
                temp=a[i][j]
                a[i][j]=a[j][n-i-1]
                a[j][n-i-1]=a[n-i-1][n-j-1]
                a[n-i-1][n-1-j]=a[n-1-j][i]
                a[n-1-j][i]=temp
                j+=1
            i+=1
        return a

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()

# } Driver Code Ends
