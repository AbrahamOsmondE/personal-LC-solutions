class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        dicti = {i:mapping[i] for i in range(10)}
        
        curr = []
        ans = []
        def backtrack(index):
            if len(curr) == len(digits):
                ans.append("".join(curr))
                return
            curr_dig = int(digits[index])
            for char in dicti[curr_dig]:
                curr.append(char)
                backtrack(index+1)
                curr.pop()
        backtrack(0)
        return ans
            
        