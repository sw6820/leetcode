class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        a,b=[],[]
        for i in range(1,int(num**0.5)+1):
            if not num%i:
                a.append(i)
                if i!=num//i:b.append(num//i)
        return sum(a)+sum(b)==2*num
        