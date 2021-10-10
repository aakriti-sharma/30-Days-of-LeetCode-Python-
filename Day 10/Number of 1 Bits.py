class Solution:
    def hammingWeight(self, n: int) -> int:
            s=str(bin(n))
            return s.count("1")
