import string
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def cnv(n,b):
            t='0123456789'
            q,r=divmod(n,b)
            return cnv(q,b)+t[r] if q else t[r]
        return sum(map(int,list(cnv(n,k))))