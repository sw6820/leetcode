class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return 2**int(log2(n))==n if n>0 else False                