
def threeSumClosest(nums, target):
    nums.sort()
    
    diff = float('inf')
    closest_target = 0

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j, k = i + 1, len(nums) - 1

        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if abs(target - s) < diff:
                diff = abs(target - s)
                closest_target = s
            
            if s < target:
                j += 1
            elif s > target:
                k -= 1
            else:
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1; k -= 1

    return closest_target


if __name__ == '__main__':
    print(threeSumClosest([-1, 2, 1, -4], 1))
    
    l = [5,-11,-7,-2,4,9,4,4,-5,12,12,-14,-5,3,-3,-2,-6,3,3,-9,4,-13,6,2,11,12,10,-14,-15,11,0,5,8,0,10,-11,-6,-1,0,4,-4,-3,5,-2,-15,9,11,
    -13,-2,-8,-7,9,-6,7,-11,12,4,14,6,-4,3,-9,-14,-12,-2,3,-8,7,-13,7,-12,-9,11,0,4,12,-6,-7,14,-1,0,14,-6,1,6,-2,-9,-4,-11,12,-1,-1,10,-7,
    -6,-7,11,1,-15,6,-15,-12,12,12,3,1,9,12,9,0,-11,-14,-1]
    print(threeSumClosest(l, 15))
    
    print(threeSumClosest([-1,2,1,-4], -100))
    print(threeSumClosest([1,1,1,0], -100))
