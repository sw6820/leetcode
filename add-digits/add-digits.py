class Solution:
    def addDigits(self, num: int) -> int:
        return 9 if not num%9 and num else num%9