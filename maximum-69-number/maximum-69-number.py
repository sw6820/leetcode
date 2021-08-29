class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        for i,v in enumerate(s):
            if v=='6':
                return int(s[:i]+'9'+s[i+1:])
        return int(s)