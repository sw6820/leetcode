class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0        
        for w in text.split():
            f=True
            for ch in w:
                if ch in list(brokenLetters):
                    f=False
                    break
            c+= 1 if f else 0                                
        return c        