class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(s[:len(c)]==c for c in words)
            