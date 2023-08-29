class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 1
        while True:
            if 0 in nums:
                nums.remove(0)
                count+=1
            else:
                break
        for i in range(count-1):
            nums += [0]
        """
        Do not return anything, modify nums in-place instead.
        """
        