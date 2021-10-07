class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        d=[]
        for i in range(0,numRows):
            d.append([])
            for j in range (0,i+1):
                d[i].append(math.comb(i,j))
        return d
