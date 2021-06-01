import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n:
            if n==1:return True
            n/=3            
        return False
        