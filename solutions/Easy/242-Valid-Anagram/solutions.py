class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = collections.Counter(s)
        for i in t:
            if counter.get(i,0) == 0:
                return False
            else:
                counter[i] -= 1
        
        for i in counter:
            if counter[i] != 0:
                return False
        return True