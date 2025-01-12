class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If the length of the string is odd, it cannot be valid
        if len(s) % 2 != 0:
            return False
        
        # Forward pass: Check if there are enough '(' to balance
        open_count = 0  # Counts '(' and unlocked positions
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                open_count += 1
            else:  # s[i] == ')' and locked[i] == '1'
                open_count -= 1
            
            if open_count < 0:  # More ')' than '('
                return False
        
        # Backward pass: Check if there are enough ')' to balance
        close_count = 0  # Counts ')' and unlocked positions
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                close_count += 1
            else:  # s[i] == '(' and locked[i] == '1'
                close_count -= 1
            
            if close_count < 0:  # More '(' than ')'
                return False
        
        # If both passes are successful, the string can be made valid
        return True
