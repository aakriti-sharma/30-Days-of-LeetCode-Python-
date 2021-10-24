class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s=0
        for i in logs:
            if i=="../":
                s=max(0,s-1)
            elif i=="./":
                continue
            else:
                s=s+1
        return s
                
