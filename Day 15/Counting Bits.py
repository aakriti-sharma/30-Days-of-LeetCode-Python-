class Solution:
    def countBits(self, n: int) -> List[int]:
        return [Counter(bin(i))["1"] for i in range(n+1)]
