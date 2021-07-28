class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a,b=[],[]
        for s,e in paths:
            a.append(s)
            b.append(e)
        for i in b:
            if i not in a: return i