class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        final = [] 
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                final.append(nums1[i])
                i += 1
            else:
                final.append(nums2[j])
                j += 1
        final = final + nums1[i:] + nums2[j:]
        size = len(final)
        return (final[size // 2]) if size % 2 != 0 else (final[size // 2 - 1] + final[size // 2]) / 2 

# Input
nums1 = list(map(int, input("Enter values for nums1 separated by spaces: ").split()))
nums2 = list(map(int, input("Enter values for nums2 separated by spaces: ").split()))

# Output
solution = Solution()
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)
