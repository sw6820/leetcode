class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = []
        for i in ops:
            if i=='+':
                if len(s) > 1: s.append(s[-1] + s[-2])
            elif i == 'C':s.pop()                
            elif i == 'D':s.append(2 * s[-1])                
            else:s.append(int(i))
                
        return sum(s)