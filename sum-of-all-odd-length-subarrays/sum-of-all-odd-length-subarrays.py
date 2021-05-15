class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        for i in range(0,len(arr)):
            for j in range(0,len(arr)-i,2):            
                s+=sum(arr[i:i+j+1])
        return s