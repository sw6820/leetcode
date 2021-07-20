from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:                
        return sorted(Counter(nums).items(), key=lambda x:-x[1])[0][0]