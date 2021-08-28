class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor=image[sr][sc]
        q=collections.deque([(sr,sc)])
        if oldColor!=newColor:
            while q:
                a,b=q.popleft()
                image[a][b]=newColor
                for x,y in [(a-1,b),(a+1,b),(a,b-1),(a,b+1)]:                    
                    if 0<=x<len(image) and 0<=y<len(image[0]) and image[x][y]==oldColor:q.append((x,y))
        return image
                