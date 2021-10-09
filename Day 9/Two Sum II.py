class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s=set(numbers)
        s=list(s)
        s.sort()
        l=[]
        for i in range(0,len(s)):
            for j in range(len(s)-1,i-1,-1):
                if s[i]+s[j]==target:
                    l.append(numbers.index(s[i])+1)
                    l.append(numbers.index(s[j])+1)
                    if l[0]==l[1]:
                        l[1]=l[0]+1
                    return l
