class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        c=collections.Counter(arr)
        for i in arr:
            if i and c[2*i] or not i and c[i]>1:return True            
        return False