# Python3 program to find pair with largest
# sum which is less than K in the array

## O(n^2) soln

# Function to find pair with largest
# sum which is less than K in the array
def Max_Sum(arr, n, k):

	# To store the break point
	p = n
	ls=arr.copy()
	# Sort the given array
	arr.sort()
	
	# Find the break point
	for i in range(0, n):
		
		# No need to look beyond i'th index
		if (arr[i] >= k):
			p = i
			break
	
	maxsum = 0
	a = 0
	b = 0
	
	# Find the required pair
	for i in range(0, p):	
		for j in range(i + 1, p):
			if(arr[i] + arr[j] < k and
			arr[i] + arr[j] > maxsum):
				maxsum = arr[i] + arr[j]
				a = arr[i]
				b = arr[j]
	x=ls.index(a)
	y=ls.index(b)
	# Print the required answer
	print(x,y)

# Driver code
arr = [5, 20, 110, 100, 10]
k = 85

n = len(arr)

# Function call
Max_Sum(arr, n, k)

# This code is contributed by Sanjit_Prasad
