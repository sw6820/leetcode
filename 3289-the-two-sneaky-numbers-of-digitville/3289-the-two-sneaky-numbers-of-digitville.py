from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [*map(lambda x:x[0],[*filter(lambda x:x[1]>1, Counter(nums).items())])]