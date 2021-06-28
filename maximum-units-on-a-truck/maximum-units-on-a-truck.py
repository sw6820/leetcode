class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        c=0
        for n,u in sorted(boxTypes, key=lambda x:-x[1]):            
            c+=(truckSize if n>truckSize else n)*u
            truckSize-=n
            if truckSize<=0: return c
        return c
        