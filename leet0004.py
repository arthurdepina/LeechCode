def findMedianSortedArrays (nums1, nums2):
    nums = sorted(nums1 + nums2)
    mid = len(nums)//2
    if len(nums)%2 == 0:
        return (nums[mid] + nums[mid - 1])/2
    else:
        return nums[mid]


# resultado_a = findMedianSortedArrays([1, 3], [2])
resultado_b = findMedianSortedArrays([1, 2], [3, 4])
# resultado_c = findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])

# print("a ->", resultado_a)
print("b ->", resultado_b)
# print("c ->", resultado_c)