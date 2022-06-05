from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        l = Counter(''.join([s.lower() for s in licensePlate if s.isalpha()]))
        s = ''
        for w in words:
            t = Counter(w)
            f=True
            for k,v in l.items():
                if t[k]<v: 
                    f=False
                    break
            if f and (s=='' or len(w)<len(s)):
                s=w
        return s