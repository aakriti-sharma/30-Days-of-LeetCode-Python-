class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for k,v in c.items():
            if v>=2:
                return True
        return False
