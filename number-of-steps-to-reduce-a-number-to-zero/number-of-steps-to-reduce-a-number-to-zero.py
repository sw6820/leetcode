class Solution:
    def numberOfSteps(self, num: int) -> int:
        c=0
        while num:            
            num=num-1 if num%2 else num//2
            c+=1
        return c
        