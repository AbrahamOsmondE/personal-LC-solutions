class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dictionary = dict()
        
        for i in stones:
            dictionary[i] = set()
        
        dictionary[0].add(0)
        
        for i in stones:
            for j in dictionary[i]:
                for step in range(j-1,j+2):
                    if step > 0 and i + step in dictionary:
                        dictionary[i+step].add(step)
        return len(dictionary[stones[-1]]) > 0