class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        for k,v in sorted(collections.Counter(nums).items(), key=lambda x:[-x[1],x[0]]):
            if not k&1:return k
        return -1