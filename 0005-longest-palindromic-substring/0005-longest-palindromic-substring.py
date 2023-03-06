class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while 0<=left and right<=len(s) and s[left]==s[right-1]:
                left-=1
                right+=1
            return s[left+1:right-1]
        if len(s)<2 or s==s[::-1]: return s
        rst=''
        for i in range(len(s)-1):
            rst=max(rst,expand(i,i+1),expand(i,i+2),key=len)
        return rst
        