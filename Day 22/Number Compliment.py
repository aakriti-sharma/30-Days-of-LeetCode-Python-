class Solution:
    def findComplement(self, num: int) -> int:
        l=list(bin(num)[2:])
        for i in range(0,len(l)):
            if l[i]=="0":
                l[i]="1"
            elif l[i]=="1":
                l[i]="0"
        return int("0b"+"".join(l),2)
