class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = [k for k,v in collections.Counter(s).items() if v==1]
        for i,c in enumerate(s):
            if c in a: return i
        return -1
            
        