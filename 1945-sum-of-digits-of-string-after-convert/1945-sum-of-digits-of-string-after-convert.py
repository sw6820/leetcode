class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # t=filter(lambda x: str(ord(x)-ord('a')+1),list(s))/
        s = ''.join([str(ord(x)-ord('a')+1) for x in s])
        for _ in range(k):
            s=sum(map(int, [*str(s)]))
        return s