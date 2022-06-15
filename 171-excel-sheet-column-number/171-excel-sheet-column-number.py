class Solution:
    def titleToNumber(self, columnTitle: str) -> int:                
        return sum((26**(len(columnTitle)-(i+1)))*(ord(c)-ord('A')+1) for i,c in enumerate(columnTitle))
            