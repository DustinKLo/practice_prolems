
def find_pivot(arr):
	print(arr)

	def traverse(left, right):
	    # base cases 
	    if right < left: 
	        return -1
	    if right == left: 
	        return left 

	    mid = int((left + right)/2) 

	    if arr[mid] > arr[mid + 1]: 
	        return mid 
	    if arr[mid] < arr[mid - 1]: 
	        return (mid-1) 
	    if arr[left] >= arr[mid]: 
	        return traverse(left, mid-1) 
	    return traverse(mid + 1, right)

	pivot = traverse(0, len(arr) - 1)

	print(pivot)
	print("")
	return pivot


if __name__ == '__main__':
	find_pivot([5,6,7,0,1,2,4])
	find_pivot([1])
	find_pivot([0,1,2,3,4,5,6,7])
	find_pivot([])
	find_pivot([1,2,3,4,5,6,7,0])
	find_pivot([1,3])
	find_pivot([3,1])
