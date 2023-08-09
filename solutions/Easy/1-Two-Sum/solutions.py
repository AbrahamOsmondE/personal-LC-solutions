class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = dict()
        for i,num in enumerate(nums):
            if num in dicti:
                return [i,dicti[num]]
            else:
                dicti[target-num] = i