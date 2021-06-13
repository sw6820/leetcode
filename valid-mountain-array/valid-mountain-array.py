class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        f=True
        if len(arr)==1 : return False
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1] or f and i==1 and arr[i-1]>arr[i] or not f and arr[i-1]<arr[i]:return False
            elif f and i!=1 and arr[i-1]>arr[i]: f=False            
        return False if f else True
                
                