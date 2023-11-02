class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        patience_sort = []
        for i in nums:
            index = bisect.bisect_left(patience_sort,i)
            
            if index == len(patience_sort):
                patience_sort.append(i)
            
            else:
                patience_sort[index] = i
        return len(patience_sort)