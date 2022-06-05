class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def distance(idx):
            d = 0
            while 1:
                if idx+d<len(s) and s[idx+d]==c or d<=idx and s[idx-d]==c:return d                                        
                else: d+=1        
        return [distance(i) for i in range(len(s))]        