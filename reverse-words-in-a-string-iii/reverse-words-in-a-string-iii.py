class Solution:
    def reverseWords(self, s: str) -> str:
        def rev(s): return s[::-1]
        return ' '.join([rev(i) for i in s.split()])