class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=''
        for i in bin(n)[2:]:
            s+='0'if int(i)&1 else'1'
        return int(s,2)