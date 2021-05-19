class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=min(len(word1),len(word2))
        s=''
        for i in range(l):
            s+=word1[i]+word2[i]
        s+=word1[l:]+word2[l:]
        return s