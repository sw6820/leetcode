class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m=-1
        for k, v in collections.Counter(arr).items():
            if k==v: m=max(m,v)
        return m
        