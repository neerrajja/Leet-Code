

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index = {}
        
        for i in range(len(nums)):
            num = nums[i] 
            
            if num in num_index and abs(i - num_index[num]) <= k:
                return True  # Found a nearby duplicate
            
            num_index[num] = i  # Update the last seen index of the number
        
        return False  # No nearby duplicate found
