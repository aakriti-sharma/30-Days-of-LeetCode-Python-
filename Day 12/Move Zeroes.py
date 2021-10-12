class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        c=nums.count(0)
        for i in range(0,c):
            nums.remove(0)
            l.append(0)
        nums.extend(l)
