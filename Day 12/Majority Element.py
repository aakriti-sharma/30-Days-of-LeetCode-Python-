class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=0
        e=0
        for i in set(nums):
            if nums.count(i)>m:
                m=nums.count(i)
                e=i
        return e 
