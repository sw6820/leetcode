from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:        
        return min(Counter(s)[k]//v for k,v in Counter(target).items())

        