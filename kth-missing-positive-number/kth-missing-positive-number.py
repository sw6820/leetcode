class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a=[1]*(arr[-1])
        a=[0]+a
        for i in arr:
            a[i]-=1
        for i in range(arr[-1]):
            if a[i]:
                k-=1
            if not k:return i
        return arr[-1]+k