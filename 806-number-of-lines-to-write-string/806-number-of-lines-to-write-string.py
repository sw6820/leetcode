class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        t=0
        rst=[0,0]
        for i in s:
            c=widths[ord(i)-ord('a')]
            if t+c<=100:
                t+=c
            else:
                rst[0]+=1
                t=c
        if t:
            rst[0]+=1
            rst[1]=t            
        return rst