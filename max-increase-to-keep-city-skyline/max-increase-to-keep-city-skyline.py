class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        l,cnt = len(grid),0
        r,c=[max(r) for r in grid],[max(c) for c in zip(*grid)]
        for i in range(l):
            for j in range(l):
                cnt+=min(r[i],c[j])-grid[i][j]
        return cnt