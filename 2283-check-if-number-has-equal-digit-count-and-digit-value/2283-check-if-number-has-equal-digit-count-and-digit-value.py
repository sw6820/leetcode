class Solution:
    def digitCount(self, num: str) -> bool:
        for k,v in collections.Counter(num).items():
            if int(k)>=len(num) or num[int(k)]!=str(v):return False                                                                 
        return True