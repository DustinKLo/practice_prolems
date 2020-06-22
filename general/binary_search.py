
def binary_search(arr, target):
	def traverse(target, left, right):
		if left > right:
			return -1
		
		mid = int((left + right) / 2)
		print(left, mid, right)
		
		if arr[mid] == target:
			return mid

		if arr[mid] < target:
			return 0 + traverse(target, mid + 1, right)
		else:
			return 0 + traverse(target, left, mid - 1)
	
	idx = traverse(target, 0, len(arr) - 1)
	print("ans: ", idx)
	return idx


if __name__ == '__main__':
	test_arr = [0,1,2,3,4,5]
	binary_search(test_arr, 3)
	print("#################\n")
	binary_search(test_arr, 0)
	print("#################\n")
	binary_search(test_arr, 5)
	print("#################\n")
	binary_search(test_arr, 6)
	print("#################\n")
	binary_search(test_arr, -100)
	print("#################\n")
	binary_search(list(range(1000)), 666)
	print("#################\n")
	binary_search(list(range(1999999)), 333)
	print("#################\n")
	binary_search([1,3], 3)

