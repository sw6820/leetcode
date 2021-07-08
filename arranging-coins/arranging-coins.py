class Solution:
    def arrangeCoins(self, n: int) -> int:
        idx=1
        while True:
            s=idx*(idx+1)//2
            if n<s: return idx-1
            elif n==s: return idx
            else: idx+=1