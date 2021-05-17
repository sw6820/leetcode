class Solution:
    def sumZero(self, n: int) -> List[int]:       
        return [*range(-(n//2),n//2+1)] if n%2 else [*range(1,n//2+1)]+[*range(-(n//2),0)]
        