class Solution:
    def secondHighest(self, s: str) -> int:                
        t=sorted(list(map(int, set([i for i in s if i.isdigit()]))))
        return t[-2] if len(t)>1 else -1