class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:        
        def isself(n):
            s=str(n)
            for i in s:                
                if not int(i) or n%int(i): return False
            return True        
        return [i for i in range(left, right+1) if isself(i)]
        