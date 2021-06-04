class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:                
        def w(s):            
            a=''            
            for i in s:
                a+=str(ord(i)-ord('a'))            
            return int(a)
        return w(firstWord)+w(secondWord)==w(targetWord)