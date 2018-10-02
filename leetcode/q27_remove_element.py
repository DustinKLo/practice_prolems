
def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    nums[:] = [i for i in nums if i != val]
    return len(nums)


if __name__ == '__main__':
    print(removeElement([0,0,1,1,1,2,2,3,3,4], 3))
    print(removeElement([1,1,1,1,1,2,2,2,3,4,5,5,5,5,6,7,10,10,20], 3))
    print(removeElement([i for i in range(100) for _ in range(3)], 3))
