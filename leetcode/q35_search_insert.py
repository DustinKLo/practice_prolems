def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    if target > nums[-1]:
        return len(nums)

    if target <= nums[0]:
    	return 0

    for i in range(1, len(nums)):
    	if nums[i] == target:
    		return i

    	if target < nums[i] and target > nums[i-1]:
    		return i

    return False


if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 5))
    print('')
    print(searchInsert([1,3,5,6], 7))
