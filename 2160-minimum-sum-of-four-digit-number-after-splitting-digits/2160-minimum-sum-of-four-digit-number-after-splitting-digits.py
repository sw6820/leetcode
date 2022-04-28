class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = sorted(list(str(num)))
        return int(n[0]+n[-1])+int(n[1]+n[2])        