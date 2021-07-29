class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n=len(matrix),len(matrix[0])
        ret=[[0 for _ in range(m)]for _ in range(n)]
        for i,row in enumerate(matrix):
            for j,col in enumerate(row):
                ret[j][i]=matrix[i][j]
        return ret