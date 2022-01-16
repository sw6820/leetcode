class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        return [ s[k*i:].ljust(k,fill) if len(s[k*i:])<k else s[k*i:k*i+k] for i in range(len(s)//k+int(bool(len(s)%k)))]