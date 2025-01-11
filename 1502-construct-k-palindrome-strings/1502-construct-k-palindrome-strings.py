class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Step 1: Manually count character frequencies
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Step 2: Count odd frequencies
        odd_count = 0
        for count in char_count.values():
            if count % 2 != 0:
                odd_count += 1

        # Step 3: Check constraints
        if k > len(s):
            return False
        if odd_count > k:
            return False

        return True
