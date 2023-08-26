class Solution:
    def longestPalindrome(self, s: str) -> str:
        LargestPalindrome = ""
        for i in range(len(s)):
            oddPalindrome = self.longestPalindromeatIndex(s,i,i)
            evenPalindrome = self.longestPalindromeatIndex(s,i,i+1)
            largerPalindrome = oddPalindrome if len(oddPalindrome) > len(evenPalindrome) else evenPalindrome
            LargestPalindrome = LargestPalindrome if len(LargestPalindrome) > len(largerPalindrome) else largerPalindrome
        return LargestPalindrome
        
    def longestPalindromeatIndex(self,s,left,right):
        leftIndex = 0
        rightIndex = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                leftIndex = left
                rightIndex = right
            else:
                break
            left -= 1
            right += 1
        return s[leftIndex:rightIndex+1]