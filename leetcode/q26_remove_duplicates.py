def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    print('starting list', nums)
    
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        if nums[0] == nums[1]:
            print([nums[0]])
            return [nums[0]]
        return nums
    
    head = nums[0]
    tail = nums[1:]
    index = 1
    
    while index < len(nums):
        if nums[index] != head:
            break
        index += 1
    
    return [head] + removeDuplicates(nums[index:])


if __name__ == '__main__':
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(removeDuplicates([1,1,1,1,1,2,2,2,3,4,5,5,5,5,6,7,10,10,20]))
    print(removeDuplicates([i for i in range(100) for _ in range(3)]))
