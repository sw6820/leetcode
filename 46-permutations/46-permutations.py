class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rst,prev=[],[]
        def dfs(ele: List[int]):
            if not ele: rst.append(prev[:])
            for e in ele:
                nxt=ele[:]
                nxt.remove(e)
                prev.append(e)
                dfs(nxt)
                prev.pop()
        dfs(nums)
        return rst