class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List
[int]:
        if len(nums) == 0:
            return []
        nums.sort()
        
        dp = [0] * (len(nums))
        
        for i, num in enumerate(nums):
            maxSubsetSize = 0
            for k in range(0, i):
                if nums[i] % nums[k] == 0:
                    maxSubsetSize = max(maxSubsetSize, dp[k])
            maxSubsetSize += 1
            dp[i] = maxSubsetSize
        
        maxSize, maxSizeIndex = max([(v, i) for i, v in enumerate
(dp)])
        ret = []
        
        # currSize: the size of the current subset
        # currTail: the last element in the current subset
        currSize, currTail = maxSize, nums[maxSizeIndex]
        for i in range(maxSizeIndex, -1, -1):
            if currSize == dp[i] and currTail % nums[i] == 0:
                ret.append(nums[i])
                currSize -= 1
                currTail = nums[i]
        
        return reversed(ret)