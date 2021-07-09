class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:        
        # return a+b+c+d-sum(list(set(a,b,c,d)))
        return sum(edges[0])+sum(edges[1])-sum(list(set(edges[0]+edges[1])))
        