class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = -1
        nums.sort()
        l = len(nums)
        for i in range(max(nums)+1):
            if l-bisect.bisect_left(nums,i)==i: return i
        return answer    