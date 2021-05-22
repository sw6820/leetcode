class Solution:
    def reverse(self, x: int) -> int:
        f=1 if x>=0 else -1
        t=int(str(abs(x))[::-1])*f
        return t if -2**31<=t<2**31 else 0
        