from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rst=[]
        a=collections.Counter(arr1)
        for i in arr2:
            rst+=[i]*a[i]
        for i in sorted(arr1):
            if i not in arr2: rst.append(i)
        return rst