        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
        
        
        dp[0] = True
        dp = [0]*(n+1)
        n = len(s)
        wordDict = set(wordDict)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
class Solution:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
                
        return dp[-1]