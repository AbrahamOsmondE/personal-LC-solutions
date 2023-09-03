class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for i in t:
            if index == len(s):
                return True
            if i == s[index]:
                index += 1
        return index == len(s)
            
        