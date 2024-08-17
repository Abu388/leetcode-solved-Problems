class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r=0
        for i in range(len(needle),len(haystack)+1):
            if haystack[r:i] == needle:
                return r  
            r+=1
        return -1