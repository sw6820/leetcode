class Solution:
    def reverseVowels(self, s: str) -> str:
        v='aeiouAEIOU'
        e=len(s)-1
        for i in range(len(s)):
            if s[i] in v:
                while i<e:
                    if s[e] in v:
                        s=s[:i]+s[e]+s[i+1:e]+s[i]+s[e+1:]                            
                        e-=1
                        break
                    else:
                        e-=1
        return s
            