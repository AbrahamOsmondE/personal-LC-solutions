class Solution:
    def countAndSay(self, n: int) -> str:
        currString = "1"
        def helper(string):
            count = 1
            current = None
            newstring = []
            for i in string:
                if current == None:
                    current = i
                elif i != current:
                    newstring.append(str(count))
                    newstring.append(current)
                    count = 1
                    current = i
                else:
                    count+=1
            newstring.append(str(count))
            newstring.append(current)
            return "".join(newstring)
        for aiudgh in range(n-1):
            currString = helper(currString)
        return currString