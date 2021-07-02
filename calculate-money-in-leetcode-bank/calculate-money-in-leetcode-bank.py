class Solution:
    def totalMoney(self, n: int) -> int:
        s,c=0,0
        for i in range((n+1)//7+1):
            for j in range(1,8):
                s+=(i+j)
                c+=1
                if c==n: return s
            