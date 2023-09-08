class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index1 = 0
        for index2 in range(len(nums)):
            if nums[index1] != nums[index2]:
                index1+=1
                nums[index1]= nums[index2]
        return index1+1
        