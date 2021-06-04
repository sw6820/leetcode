class Solution:
    def replaceDigits(self, s: str) -> str:
        a=''
        for i,v in enumerate(s):            
            a+=chr(ord(s[i-1])+int(v)) if i%2 else v
        return a
        