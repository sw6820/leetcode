class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        a=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    if words[i] in words[j] and words[i]!=words[j]:
                        a.append(words[i])
        return list(set(a))