class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return 4**(log2(n)//2)==n if n>0 else False