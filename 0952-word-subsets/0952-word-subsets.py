class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        req_freq = {}
        for word in words2:
            for char in word:
                count = word.count(char)
                if char in req_freq:
                    req_freq[char] = max(req_freq[char], count)
                else:
                    req_freq[char] = count
        
        result = []
        for word in words1:
            is_universal = True
            for char,freq in req_freq.items():
                if word.count(char)<freq:
                    is_universal = False
                    break
            if is_universal:
                result.append(word)
        return result
        