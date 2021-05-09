from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a=Counter(sentence)        
        return len(a)==26 and 0 not in a.values()