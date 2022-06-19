class Solution:
    def findComplement(self, num: int) -> int:        
        return (pow(2,(len(bin(num))-2))-1)^num