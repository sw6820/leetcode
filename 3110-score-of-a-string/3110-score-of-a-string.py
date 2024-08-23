class Solution:
    def scoreOfString(self, s: str) -> int:
        # return sum(abs(ord(s[i])-ord(s[i+1])) for i in range(len(s)-1))
        return sum(map(lambda x: abs(ord(x[0]) - ord(x[1])), zip(s, s[1:])))
        