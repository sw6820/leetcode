class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return len(max(sentences, key=lambda x:len(x.split())).split())