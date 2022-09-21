class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        rst=[]        
        def dfs(p,s):
            if s==len(graph)-1:rst.append(p[:])
            for i in graph[s]:                
                p.append(i)                
                dfs(p,i)
                p.pop()
        dfs([0],0)        
        return rst