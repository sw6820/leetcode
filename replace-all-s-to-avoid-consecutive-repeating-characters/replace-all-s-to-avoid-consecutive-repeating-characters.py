class Solution:
    def modifyString(self, s: str) -> str:
        t=''
        for i,v in enumerate(s):
            if v=='?':
                if i!=len(s)-1 and s[i+1]=='a':
                    if t and t[-1]=='b':t+='c'                        
                    else:
                        if t and t[-1]=='a': 
                            if s[i+1]=='b': t+='c'
                            else: t+='b'
                        else: t+='b'
                else:
                    if t and t[-1]=='a': 
                        if i!=len(s)-1 and s[i+1]=='b':t+='c'
                        else: t+='b'                        
                    else: 
                        if i!=len(s)-1 and s[i+1]=='a': t+='b'
                        else: t+='a'
            else: t+=v
        return t
                