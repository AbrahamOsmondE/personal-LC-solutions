class Solution:
    def firstMissingPositive(self, nums):
        s = set(nums)
        n = len(nums)
        for i in range(1,n+1):
            if i not in s:
                return i
        return n+1