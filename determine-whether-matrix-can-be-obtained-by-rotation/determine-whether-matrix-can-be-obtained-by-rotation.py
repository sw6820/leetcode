class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        t=mat       
        def rotate(tmp):                        
            a=[[0 for _ in range(n)]for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    a[i][j]=tmp[j][n-1-i]            
            print(a)
            return a            
        for _ in range(4):
            k=rotate(t)
            if k==target: return True
            t=k
        return False