class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return[ i for i in list(set(nums1)) if i in nums2]