class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        w=[]
        for i in words:
            s=''
            for c in i:
                s+=a[ord(c)-ord('a')]    
            w.append(s)
        return len(set(w))