        line[-1][1] = 0
        spaceLeft +=lastSpaces
        totalWords = len(line)
        return sentence
    
    def adjustSpaces(self, line, spaceLeft):
        lastSpaces = line[-1][1]
        sentence = ''
        for word, spaceCount in line:
            sentence+=word
            sentence+=' '*spaceCount
            
class Solution:
    def createSentence(self, line):
        
        if totalWords == 1:
            line[0][1] = spaceLeft
            return self.createSentence(line)
        
        for i in range(totalWords-1, 0, -1):
            spaceAfterWord = spaceLeft//i
            spaceLeft-=spaceAfterWord
            
            line[i-1][1] += spaceAfterWord
            
        return self.createSentence(line)    
        
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        cUsage = 0