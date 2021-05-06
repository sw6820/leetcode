class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:        
        s=0
        for i in set(jewels):
            s+=stones.count(i)
        return s