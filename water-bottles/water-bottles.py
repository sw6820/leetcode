class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        s=numBottles
        while numBottles>=numExchange:
            s+=(numBottles//numExchange)
            numBottles=numBottles//numExchange + numBottles%numExchange
        return s