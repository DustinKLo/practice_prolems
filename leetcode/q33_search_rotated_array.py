
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    l = 0 # left boundary
    r = len(nums) - 1 # right boundary
    print('target: {}'.format(target))
    
    counter = 0
    while r - l >= 0:
        m = (r + l)/2 # midpoint of array
        left = nums[l:m]
        right = nums[m:r]

        print('left: {} \t right: {}'.format(left, right))
        print('left index: {} \t mid index: {} \t right index: {} \n'.format(l, m, r, counter))


        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        elif nums[m] == target:
            return m


        if nums[l] <= nums[m]: # left most number is less than mid number
        	pass
        else:
        	pass
        

        counter += 1
        if counter % 7 == 0:
            break

    return -1



if __name__ == '__main__':
    print(search([4,5,6,7,8,9,10,11,12,13,14,15,0,1,2], 14))
    print('\n')
    print('\n')
    print(search([4,5,6,7,8,9,10,11,12,13,14,15,0,1,2], 15))
    print('\n')
    print('\n')
    print(search([4,5,6,7,8,9,10,11,12,13,14,15,0,1,2], 8))
    print('\n')
    print('\n')
    print(search([4,5,6,7,8,9,10,11,12,13,14,15,0,1,2], 1))
    print('\n')
    print('\n')
    print(search([4,5,6,7,8,9,10,11,12,13,14,15,0,1,2], 0))
    print('\n')
    print('\n')
    print(search([4,5,6,7,8,9,10,11,12,13,14,15,0,1,2], 2))
