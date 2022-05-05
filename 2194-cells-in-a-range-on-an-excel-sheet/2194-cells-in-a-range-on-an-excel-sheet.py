class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        rst = []
        r,c=s.split(':')
        for i in range(ord(r[0]),ord(c[0])+1):
            for j in range(int(r[1:]),int(c[1:])+1):
                rst.append(chr(i)+str(j))    
        return rst