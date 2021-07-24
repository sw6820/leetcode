class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l=len(arr)
        for k,v in collections.Counter(arr).items():
            if 4*v>l: return k