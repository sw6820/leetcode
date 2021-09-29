class Solution:
    def freqAlphabets(self, s: str) -> str:
        idx=0
        t=''
        while idx<len(s):
            if s[idx] in ['1','2'] and idx+2<len(s) and s[idx+2]=='#':
                t+=chr(int(s[idx:idx+2])-1+ord('a'))
                idx+=3
            else:
                t+=chr(int(s[idx])-1+ord('a'))
                idx+=1        
        return t
                