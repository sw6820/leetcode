class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:        
        return ord(coordinates[0])&1!=int(coordinates[1])&1