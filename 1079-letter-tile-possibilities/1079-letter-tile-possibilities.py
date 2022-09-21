class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        c,prev=set(),[]        
        def dfs(ele):            
            c.add(''.join(prev))            
            for t in ele:
                nxt=ele[:]
                nxt.remove(t)
                prev.append(t)
                dfs(nxt)                
                prev.pop()        
        dfs([*tiles])        
        return len(c)-1