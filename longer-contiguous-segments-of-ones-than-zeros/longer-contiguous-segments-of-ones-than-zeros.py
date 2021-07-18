class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        o,z=0,0
        i=0
        while i<len(s):
            e=i
            while e<len(s):
                if s[i]==s[e]:e+=1                    
                else:
                    if s[i]=='1':o=max(o,e-i)                        
                    else:z=max(z,e-i)                        
                    break
            if e>=len(s):
                if s[i]=='1':o=max(o,e-i)
                else:z=max(z,e-i)
                break
            i=e        
        return o>z