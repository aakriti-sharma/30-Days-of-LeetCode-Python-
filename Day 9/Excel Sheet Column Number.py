class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n=0
        for i in columnTitle:
            n=n*26+ord(i)-64
        return n
