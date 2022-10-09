class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum(not gcd(a,b)%i for i in range(1,gcd(a,b)+1))