class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_index = 0
        for i in range(len(nums)):
            if i > maximum_index:
                return False
            maximum_index = max(maximum_index,i+nums[i])
        return True