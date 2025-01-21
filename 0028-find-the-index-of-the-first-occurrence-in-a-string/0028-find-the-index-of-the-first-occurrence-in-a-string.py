class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1


        haystack_length = len(haystack)
        needle_length = len(needle)

        for i in range(haystack_length - needle_length+1):

            #compare charachter by character
            match = True
            for j in range(needle_length):
                if haystack[i+j] != needle[j]:
                    match = False
                    break


            if match:
                return i
        
        return -1




        