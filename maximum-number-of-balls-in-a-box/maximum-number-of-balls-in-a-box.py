class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:                
        return max(collections.Counter([sum(map(int,str(i))) for i in range(lowLimit, highLimit+1)]).values())