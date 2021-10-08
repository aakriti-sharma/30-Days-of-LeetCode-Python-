class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        op=""
        while columnNumber>0:
            n=columnNumber%26
            if n==0:
                op=op+chr(64+26)
                columnNumber=columnNumber//26-1
            else:
                op=op+chr(64+n)
                columnNumber=columnNumber//26
        return op[::-1]
