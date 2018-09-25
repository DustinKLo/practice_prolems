
def threeSum2(nums):
    ans = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j, k = i + 1, len(nums) - 1

        while j < k:
            print('{}:{} \t {}:{} \t {}:{}'.format(i, nums[i], j, nums[j], k, nums[k]))
            s = nums[i] + nums[j] + nums[k]
            if s < 0:
                j += 1
            elif s > 0:
                k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1; k -= 1

    return ans


if __name__ == '__main__':
    print(threeSum2([-1, 0, 1, 2, -1, -4]))
    print('\n')

    l = [5,-11,-7,-2,4,9,4,4,-5,12,12,-14,-5,3,-3,-2,-6,3,3,-9,4,-13,6,2,11,12,10,-14,-15,11,0,5,8,0,10,-11,-6,-1,0,4,-4,-3,5,-2,-15,9,11,
    -13,-2,-8,-7,9,-6,7,-11,12,4,14,6,-4,3,-9,-14,-12,-2,3,-8,7,-13,7,-12,-9,11,0,4,12,-6,-7,14,-1,0,14,-6,1,6,-2,-9,-4,-11,12,-1,-1,10,-7,
    -6,-7,11,1,-15,6,-15,-12,12,12,3,1,9,12,9,0,-11,-14,-1]
    # print(threeSum(l))
    print(threeSum2(l))
