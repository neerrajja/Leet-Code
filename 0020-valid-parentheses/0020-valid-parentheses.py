class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                # Check if the top of the stack matches
                top_element = stack.pop() if stack else '#'  # Use '#' as a placeholder for empty stack
                if bracket_map[char] != top_element:
                    return False
            else:  # It's an opening bracket
                stack.append(char)
        
        # Stack should be empty if all brackets are matched
        return not stack
'''
class Solution:
    def isValid(self, s: str) -> bool:
        round_count = 0
        curly_count = 0
        square_count = 0

        for i in s:
            if i == '(':
                round_count += 1
            elif i == ')':
                round_count -= 1
            elif i == '{':
                curly_count += 1
            elif i == '}':
                curly_count -= 1
            elif i == '[':
                square_count += 1
            elif i == ']':
                square_count -= 1

            # If any count goes negative, it's invalid
            if round_count < 0 or curly_count < 0 or square_count < 0:
                return False

        # All counts must be zero for valid parentheses
        return round_count == 0 and curly_count == 0 and square_count == 0
'''
