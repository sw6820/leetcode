class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        l=[]
        for i in range(len(candies)):
           l.append((candies[i]+extraCandies)>=m)
        return l
        