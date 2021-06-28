class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=collections.Counter(s)
        f=False
        cnt=0
        for k,v in c.items():
            if v%2: f=True
            cnt+=v//2
        return cnt*2 + int(f)