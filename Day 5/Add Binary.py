class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]      #if .replace("0b","") instead of [2:] runtime decreases by 15 ms
