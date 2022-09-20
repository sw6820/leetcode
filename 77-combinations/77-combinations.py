class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        rst = []
        def dfs(ele,s,k):
            if not k:rst.append(ele[:])
            for e in range(s,n+1):
                ele.append(e)
                dfs(ele,e+1,k-1)
                ele.pop()
        dfs([],1,k)
        return rst