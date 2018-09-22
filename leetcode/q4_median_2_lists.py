


# last step of merge sort, putting it all together one by one
def findMedianSortedArrays(nums1, nums2):
    i = 0 # index for nums1
    j = 0 # index for nums2

    combined = []
    while i < len(nums1) and j < len(nums2):
        if i >= len(nums1) or j >= len(nums2):
            break

        if nums1[i] <= nums2[j]:
            combined.append(nums1[i])
            i += 1
        else:
            combined.append(nums2[j])
            j += 1

    if i >= len(nums1):
        leftovers = nums2[j:]
    else:
        leftovers = nums1[i:]

    combined += leftovers
    print combined

    if len(combined) % 2 == 0:
        midpoint = len(combined) / 2 - 1
        return float(combined[midpoint] + combined[midpoint+1])/2
    else:
        midpoint = len(combined) / 2
        return combined[midpoint]

nums1 = [1, 2,3,4,5,6,7,8,9]
nums2 = list(range(15,30))
findMedianSortedArrays(nums1, nums2)
