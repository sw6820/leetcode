class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        t=Counter([min(i) for i in rectangles])        
        return t[max(t.keys())]