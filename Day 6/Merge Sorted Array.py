class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in nums2:
            nums1[m]=i
            m=m+1
        nums1.sort()
