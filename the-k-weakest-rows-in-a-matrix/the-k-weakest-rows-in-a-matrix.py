class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        tmp,ret=[],[]
        def bisearch(row):
            s,e=0,len(row)-1
            while s<e:
                m=(s+e)//2
                if row[m]:s=m+1
                else: e=m
            return len(row) if row[-1] else s
        for i,row in enumerate(mat):
            tmp.append([row,i])
        for i in sorted(tmp)[:k]:
            ret.append(i[1])
        return ret
                