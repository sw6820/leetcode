class Solution:    
    def maxDistinct(self, s: str) -> int:
        # from collections import defaultdict
        # d=defaultdict(bool)
        # for c in s:
        #     if not d[c]:
        #         d[c]=True
        # return len(d)
        # return len(set(s))
        visit=[0]*26
        for i in s:
            visit[int(ord(i))-int(ord('a'))]=1
        return sum(visit)

        

        