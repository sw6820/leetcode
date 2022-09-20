class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rst=[]
        def dfs(idx,p):
            rst.append(p)
            for i in range(idx,len(nums)):
                dfs(i+1,p+[nums[i]])
        dfs(0,[])
        return rst