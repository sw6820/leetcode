class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        S=s[::-1]
        st=set(s)
        for i in range(26):
            if chr(ord('a')+i) not in st:continue
            if (len(s)-S.index(chr(ord('a')+i)))-s.index(chr(ord('a')+i))-2!=distance[i]:return 0            
        return 1            