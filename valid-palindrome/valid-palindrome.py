class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=''
        for i in s.lower():
            if i.isalpha() or i.isnumeric():k+=i                
        return k==k[::-1]