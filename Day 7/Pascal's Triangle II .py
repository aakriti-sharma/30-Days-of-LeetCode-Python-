class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l=[]
        for i in range(0,rowIndex+1):
            l.append(math.comb(rowIndex,i))
        return l
