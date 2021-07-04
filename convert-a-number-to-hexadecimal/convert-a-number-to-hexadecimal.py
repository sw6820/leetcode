class Solution:
    def toHex(self, num: int) -> str:        
        return hex(num+(0 if num>=0 else 2**32))[2:]