
def fourSumClosest(nums, target):
    length = len(nums)
    if length == 4:
        if sum(nums) == target:
            return [nums]
        else:
            return []
    if length < 4:
        return []
    
    nums.sort()
    ans = []
    sets = []

    for i in range(length - 3):
        for j in range(i + 1, length - 2):
            
            k = j + 1
            l = length - 1 
            while k < l:
                s = nums[i] + nums[j] + nums[k] + nums[l]
                print('index: [{} {} {} {}] \t values: [{} {} {} {}]\t sum: {}'.format(i,j,k,l, nums[i], nums[j], nums[k], nums[l], s))
                
                if s == target:
                    arr = [nums[i], nums[j], nums[k], nums[l]]
                    if set(arr) not in sets:
                        ans.append(arr)
                        sets.append(set(arr))

                if s < target:
                    k += 1
                elif s > target:
                    l -= 1
                else:
                    while k < l and nums[k] == nums[k+1]:
                        k += 1
                    while k < l and nums[l] == nums[l-1]:
                        l -= 1
                    k += 1; l -= 1

    print(nums)
    return ans


if __name__ == '__main__':
    print(fourSumClosest([-3,-2,-1,0,0,1,2,3], 0))
    print(fourSumClosest([0,0,0,0], 0))
