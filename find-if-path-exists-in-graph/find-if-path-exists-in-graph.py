class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        p=[i for i in range(n)]
        def find(x):
            if x==p[x]:return x
            p[x]=find(p[x])
            return p[x]
        def union(x,y):
            x,y=find(x),find(y)
            if x!=y:p[max(x,y)]=min(x,y)
        def isUnion(x,y): return find(x)==find(y)
        for a,b in edges:union(a,b)
        return isUnion(start,end)
            
        
                
                
        