class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d=[0]*len(cost)
        d[0],d[1]=cost[0],cost[1]
        for i in range(2,len(cost)):
            d[i]=min(d[i-1],d[i-2])+cost[i]        
        return min(d[-1],d[-2])