class Solution:
    def isUgly(self, n: int) -> bool:
        ugly=[2,3,5]
        idx=0
        while n>1 and idx<3:
            if not n%ugly[idx]:n//=ugly[idx]
            else: idx+=1
        return n==1