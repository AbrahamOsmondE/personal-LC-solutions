class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        ans = float('-inf')
        for i in nums:
            currSum += i
            ans = max(currSum,ans)
            if currSum < 0:
                currSum = 0
        return ans