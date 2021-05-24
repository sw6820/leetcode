class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        s,n=0,len(grid)
        s+=n*n*2
        dr=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(n):
            for j in range(n):
                for dx,dy in dr:
                    x,y=i+dx,j+dy
                    if x<0 or x==n or y<0 or y==n:s+=grid[i][j]
                    else:
                        t=grid[i][j]-grid[x][y]
                        if t>0:s+=t
        print(s)
        for i in grid:
            s-=i.count(0)*2
        return s
        