class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t=''.join(map(str,digits))        
        return map(int,list(str(int(t)+1)))