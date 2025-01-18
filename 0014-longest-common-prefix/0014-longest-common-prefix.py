class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #Sorting the given list
        strs.sort()

        #taking the first and last words for comparing
        first = strs[0]
        last = strs[-1]
        common_prefix = []

        #iterating through the list
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                common_prefix.append(first[i])
            else:
                break
        
        return "".join(common_prefix)




        