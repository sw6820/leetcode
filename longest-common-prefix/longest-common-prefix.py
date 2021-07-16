class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        s=min(strs, key=len)
        for i,c in enumerate(s):
            for st in strs:
                if st[i]!=c: return s[:i]
        return s