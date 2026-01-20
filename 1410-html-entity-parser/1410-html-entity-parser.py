class Solution:    
    def entityParser(self, text: str) -> str:
        d = {"&quot;": '"', "&apos;": "'", "&amp;":"&","&gt;":">","&lt;":"<","&frasl;":"/"}
        s,L=0,len(text)
        result = ''
        while s<L:
            t=text[s]
            if t=='&':
                f=1
                for e in range(s+1,min(s+7,L)):
                    if text[e]==';':
                        tmp=text[s:e+1]
                        if tmp in d:
                            result+= d[tmp]
                            s=e
                        else:result+=t                            
                        f=0
                        break
                if f:result+=t
            else:result+=t       
            s+=1
            
        return result

# "and I quote: &quot;...&quot;"
# "leetcode.com&frasl;problemset&frasl;all"        
# "&&gt;"
# "&&&"