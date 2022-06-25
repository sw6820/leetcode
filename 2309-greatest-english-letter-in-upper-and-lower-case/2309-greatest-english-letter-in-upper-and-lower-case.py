class Solution:
    def greatestLetter(self, s: str) -> str:
        low,up=[0]*26,[0]*26        
        for i in s:
            if i.isupper():up[ord(i)-ord('A')]+=1                
            else:low[ord(i)-ord('a')]+=1                
        for i in range(25,-1,-1):
            if up[i] and low[i]:return chr(i+ord('A'))
        return ''