class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        a=sum(1 for i in position if i%2)
        return min(a,len(position)-a)