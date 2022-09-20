class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rst=[]
        def dfs(cs,idx,p):
            if cs<0:return
            if not cs:
                rst.append(p)
                return
            for i in range(idx,len(candidates)):
                dfs(cs-candidates[i],i,p+[candidates[i]])
        dfs(target,0,[])
        return rst