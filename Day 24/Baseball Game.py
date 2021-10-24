class Solution:
    def calPoints(self, ops: List[str]) -> int:
        p=[]
        for i in ops:
            if (i.strip("-")).isnumeric():
                p.append(int(i))
            elif i=="+":
                p.append(p[-1]+p[-2])
            elif i=="C":
                p.pop()
            elif i=="D":
                p.append(p[-1]*2)
            print(p)
        return sum(p)
            
        
