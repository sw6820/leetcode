class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt=0
        l=0
        for i in s:
            l+=(1 if i=='R' else -1)
            if not l:cnt+=1
        return cnt