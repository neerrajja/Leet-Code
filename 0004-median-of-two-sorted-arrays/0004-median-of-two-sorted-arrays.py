class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = nums1 + nums2
        merged_nums.sort()
        length = len(merged_nums)
        mid = length//2
        if length%2 == 0:
            median = (merged_nums[mid] + merged_nums[mid-1])/2
        else:
            median = merged_nums[mid]
        return median