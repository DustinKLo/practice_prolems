class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        print("sorted", nums)
        print("target", target)
        print("")

        closest_distance = float('inf')
        closest = 0


        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    print("ans", total)
                    return total

                print([nums[i], nums[j], nums[k]], total)
                print("target:", target, "distance from target:", abs(target - total))
                if abs(target - total) < closest_distance:
                    closest_distance = abs(target - total)
                    closest = total

                if total < target:
                    j += 1
                else:
                    k -= 1

        print("ans", closest)
        return closest


if __name__ == '__main__':
    s = Solution()
    s.threeSumClosest([-1, 2, 1, -4], 1)
    print("#############\n")

    s.threeSumClosest([1,1,-1,-1,3], -1)
    print("#############\n")
    
    l = [5,-11,-7,-2,4,9,4,4,-5,12,12,-14,-5,3,-3,-2,-6,3,3,-9,4,-13,6,2,11,12,10,-14,-15,11,0,5,8,0,10,-11,-6,-1,0,4,-4,-3,5,-2,-15,9,11,
    -13,-2,-8,-7,9,-6,7,-11,12,4,14,6,-4,3,-9,-14,-12,-2,3,-8,7,-13,7,-12,-9,11,0,4,12,-6,-7,14,-1,0,14,-6,1,6,-2,-9,-4,-11,12,-1,-1,10,-7,
    -6,-7,11,1,-15,6,-15,-12,12,12,3,1,9,12,9,0,-11,-14,-1]
    s.threeSumClosest(l, 15)
    print("#############\n")

    s.threeSumClosest([1,1,1,0], -100)
    print("#############\n")
    
    s.threeSumClosest([0,2,1,-3], 1)
    print("#############\n")

    s.threeSumClosest([1,2,4,8,16,32,64,128], 82)
