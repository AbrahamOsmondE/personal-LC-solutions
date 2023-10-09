class Solution:
    def romanToInt(self, s: str) -> int:
        dictionar = {'I':1,'V':5,"X":10,
'L':50,'C':100,'D':500,'M':1000}
        output = 0
        letters = list(s)
        for i in range(len(letters)):
            try:
                if dictionar[letters[i]
] < dictionar[letters[i+1]]:
                    output = output - 
dictionar[letters[i]]
                else:
                    output = output + 
dictionar[letters[i]]
            except:
                output = output + 
dictionar[letters[i]]
        return output
            
            
            
            