class Solution:
    def convert(self, s: str, numRows: int) -> str:
        hasher = {}
        start = 1
        leap = 1
        if numRows == 1:
            return s
        for i in range(1,numRows+1):
            hasher[i] = []
        for x in s:
            if start == 1:
                leap = 1
            elif start == numRows:
                leap = -1
            hasher[start].append(x)
            start += leap
        zigzag = []
        for i in range(1,numRows+1):
            zigzag.extend(hasher[i])
        return "".join(zigzag)
            
            