class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        t=collections.Counter(s)
        c=t[s[0]]
        for i,v in t.items():
            if c!=v: return False
        return True