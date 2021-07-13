class Solution:
    def convertToBase7(self, num: int) -> str:         
        if not num: return str(num)
        t = '0123456'
        k=abs(num)
        s=''
        while abs(k):
            q, r = divmod(abs(k), 7)
            s += t[r]
            k = q
        return ('-' if num < 0 else '')+s[::-1]