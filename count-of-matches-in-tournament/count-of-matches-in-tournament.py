class Solution:
    def numberOfMatches(self, n: int) -> int:
        s=0
        while n>1:
            s+=n//2
            n=n//2+1 if n%2 else n//2
        return s
        