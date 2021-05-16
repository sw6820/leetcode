class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        for i,v in enumerate(mat):
            s+=v[i]
            s+=(v[len(mat)-i-1] if len(mat)!=2*i+1 else 0)
        return s