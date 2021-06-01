class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1: return 1
        G,R=[[]for _ in range(n+1)],[[]for _ in range(n+1)]
        for i,v in trust:
            G[v].append(i)
            R[i].append(v)
        for i,v in enumerate(G):
            if len(v)==n-1: 
                return -1 if R[i] else i
        return -1
            