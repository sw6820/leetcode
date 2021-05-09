class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=list(str(n))
        m=[*map(int,s)]
        a=1
        for i in m:
           a*=i
        return a-sum(m)