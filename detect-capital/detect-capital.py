class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        f=word[0].isupper()
        c=sum(1 for i in word if i.isupper())
        return f and c==1 or not c or c==len(word)
        # return word.islower() or word.isupper() or word.istitle()