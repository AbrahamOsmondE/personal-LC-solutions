class Solution:
    def longestValidParentheses(self, s: str) -> int:
        bracketStack = [-1]
        maxLength = 0
        for index,bracket in enumerate(s):
            if bracket == '(':
                bracketStack.append(index)
            elif bracket == ')':
                indexCurrent = bracketStack.pop()
                if len(bracketStack) == 0:
                    bracketStack.append(index)
                else:
                    maxLength = maxLength if maxLength > abs(index - 
bracketStack[-1]) else index -bracketStack[-1]
        return maxLength
                            
                        
                
            
                
        