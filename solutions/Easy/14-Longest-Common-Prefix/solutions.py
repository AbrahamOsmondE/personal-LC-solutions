class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,char in enumerate(s1):
            if s2[i] != char:
                return s1[:i]
        return s1
        