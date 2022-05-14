class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        t=collections.Counter(arr)        
        return len(set(t.values()))==len(t)