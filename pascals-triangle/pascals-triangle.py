class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        d=[[0 for _ in range(i+1)]for i in range(numRows)]        
        print(d)
        for i in range(numRows):
            for j in range(i+1):                
                d[i][j]=1 if j==i or j==0 else d[i-1][j]+d[i-1][j-1]        
        return d