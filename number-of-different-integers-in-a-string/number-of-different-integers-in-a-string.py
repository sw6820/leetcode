class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        a=[]
        s,e=-1,0
        while s<len(word) and e<len(word):
            s+=1
            if s<len(word) and word[s].isdigit():
                e=s
                while True:
                    e+=1
                    if e>=len(word):
                        a.append(int(word[s:]))
                        return len(set(a))
                    if word[e].isalpha():
                        a.append(int(word[s:e]))
                        s=e
                        break
        return len(set(a))