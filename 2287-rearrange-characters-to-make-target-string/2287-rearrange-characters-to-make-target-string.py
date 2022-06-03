from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:        
        s=Counter(s)
        return min(s[k]//v for k,v in Counter(target).items())

        