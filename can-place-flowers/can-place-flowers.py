class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):            
            if not n: return True
            if i==0 and not flowerbed[0]and (len(flowerbed)==1 or not flowerbed[1]):
                flowerbed[0]+=1
                n-=1
            elif i==len(flowerbed)-1 and not flowerbed[-1] and not flowerbed[-2]:
                flowerbed[-1]+=1
                n-=1
            elif 0<i<len(flowerbed)-2 and not sum(flowerbed[i-1:i+2]): 
                flowerbed[i]+=1
                n-=1
        return False if n else True
            