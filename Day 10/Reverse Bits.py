class Solution:
    def reverseBits(self, n: int) -> int:
        b=str(bin(n))
        b=b.replace("0b","")
        b=b[::-1]
        while(len(b)<32):
            b=b+"0"
        return int("0b"+b,2)
