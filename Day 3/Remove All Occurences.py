class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=nums.count(val)
        while c>0:
            nums.remove(val)
            c=c-1
        return len(nums)
