class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        max_sum = 0
        current_sum = nums[0]

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                current_sum += nums[i+1]
            else:
                max_sum = max(current_sum, max_sum)
                current_sum = nums[i+1]

        max_sum = max(max_sum, current_sum)
        return max_sum

        