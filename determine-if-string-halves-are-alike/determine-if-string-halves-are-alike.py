class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c=0
        v=['a','e','i','o','u']
        for i in s.lower()[:len(s)//2]:
            if i in v: c+=1
        for i in s.lower()[len(s)//2:]:
            if i in v: c-=1
        return c==0