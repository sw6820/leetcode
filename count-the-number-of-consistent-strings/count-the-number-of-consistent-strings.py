class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        f,s=True,0
        for w in words:
            for j in w:
                if j not in allowed: 
                    f=False
                    break
            if f: s+=1
            else: f=True
        return s
            
            
                    