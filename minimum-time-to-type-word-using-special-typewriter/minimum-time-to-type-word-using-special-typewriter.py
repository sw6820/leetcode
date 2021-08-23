class Solution:
    def minTimeToType(self, word: str) -> int:
        t=ord('a')
        c=0
        for i in word:
            k=abs(t-ord(i))
            c+=min(k,26-k)+1
            t=ord(i)
        return c