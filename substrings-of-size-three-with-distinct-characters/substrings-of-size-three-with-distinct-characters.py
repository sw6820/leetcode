class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        for i in range(len(s)-2):
            t=s[i:i+3]
            if max(collections.Counter(t).values())==1: c+=1
        return c