class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            c=nums.count(nums[i])
            if c>1:
                while c>1:
                    del nums[i]
                    c=c-1
            i=i+1
        return len(nums)
