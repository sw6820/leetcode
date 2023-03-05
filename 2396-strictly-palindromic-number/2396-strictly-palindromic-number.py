class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def nth(n,base):
            rst=[]
            while n:
                q,r=divmod(n,base)
                rst.append(r)
                n=q
            return rst==rst[::-1]
        for b in range(2,n-1):
            if not nth(n,b): return False
        return True
        