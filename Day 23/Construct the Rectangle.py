class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        s=int(math.sqrt(area))
        while s>0:
            if area%s==0:
                return [area//s,s]
            s=s-1
        
