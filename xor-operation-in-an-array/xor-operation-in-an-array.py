class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a=[start+2*i for i in range(n)]
        k=a[0]
        for j in range(1,n):
            k^=a[j]
        return k