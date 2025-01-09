'''
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s
'''

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        count = 0
        pref_len = len(pref)

        for word in words:
            if word[:pref_len] == pref:
                count += 1
        return count
        
