class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = collections.Counter(magazine)
        for k,v in collections.Counter(ransomNote).items():
            if m[k]<v : return False        
        return True