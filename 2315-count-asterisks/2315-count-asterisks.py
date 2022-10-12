class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(w.count('*') for i,w in enumerate(s.split('|')) if not i&1)