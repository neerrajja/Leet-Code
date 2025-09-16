from typing import List
import math

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            # Keep merging the top of the stack with current num while they are non-coprime
            while stack:
                gcd_value = math.gcd(stack[-1], num)
                if gcd_value == 1:
                    break  # They are coprime, no merge needed
                
                # Compute LCM and update num
                num = (stack.pop() * num) // gcd_value
            
            # Push the current number (merged if needed) to the stack
            stack.append(num)
        
        return stack
