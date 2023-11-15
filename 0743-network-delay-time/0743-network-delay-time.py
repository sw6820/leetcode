class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G,D=defaultdict(list),defaultdict(int)        
        for u,v,w in times:
            G[u].append((v,w))
        c,m,q=0,0,[(0,k)]
        while q:
            t,u=heapq.heappop(q)
            if u not in D:
                D[u]=t
                m=max(m,t)
                c+=1
                for v,w in G[u]:
                    heapq.heappush(q,(t+w,v))        
        return m if c==n else -1
###    