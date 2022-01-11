class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        n=list(set(nums1)) + list(set(nums2)) + list(set(nums3))        
        return [i for i in set(n) if n.count(i)>1]