class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i,v in enumerate(sentence.split()):
            if v[:len(searchWord)]==searchWord: return i+1
        return -1