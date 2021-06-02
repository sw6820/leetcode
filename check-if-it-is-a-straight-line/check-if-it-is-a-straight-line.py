class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        c=coordinates
        if c[0][0]==c[1][0]:
            for i in range(1,len(c)):
                if c[0][0]!=c[i][0]:return False
            return True
        else:            
            u,d=(c[1][1]-c[0][1]),(c[1][0]-c[0][0])                   
            for i in range(1,len(c)):
                if d*(c[i][1]-c[0][1])!=u*(c[i][0]-c[0][0]): return False
            return True            