class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backTrack(s,left,right):
            if len(s) == 2*n:
                ans.append("".join(s))
            if left < n:
                s.append("(")
                backTrack(s,left+1,right)
                s.pop()
            if right < left:
                s.append(")")
                backTrack(s,left,right+1)
                s.pop()
        backTrack([],0,0)
        return ans