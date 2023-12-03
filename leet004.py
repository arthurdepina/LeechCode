def findMedianSortedArrays (nums1, nums2):
    nums = sorted(nums1 + nums2)
    if len(nums)%2 == 0:
        print((nums[len(nums)//2] + nums[len(nums)//2 - 1])/2)
        return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
    else:
        return nums[len(nums)//2]


# resultado_a = findMedianSortedArrays([1, 3], [2])
resultado_b = findMedianSortedArrays([1, 2], [3, 4])
# resultado_c = findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])

# print("a ->", resultado_a)
print("b ->", resultado_b)
# print("c ->", resultado_c)