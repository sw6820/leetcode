class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(0.5*abs(x[0]*y[1]+y[0]*z[1]+z[0]*x[1]-(x[1]*y[0]+y[1]*z[0]+z[1]*x[0])) for x,y,z in itertools.combinations(points, 3))