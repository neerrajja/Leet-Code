class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split()
        last_word = temp[-1]
        return len(last_word)
        