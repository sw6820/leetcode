class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum(-int(c) if i&1 else int(c) for i,c in enumerate(str(n)))