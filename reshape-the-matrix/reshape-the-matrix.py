class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(mat)*len(mat[0]):return mat
        rst=[[0 for _ in range(c)]for _ in range(r)]
        idx=0
        for row in mat:
            for col in row:
                rst[idx//c][idx%c]=col
                idx+=1
        return rst