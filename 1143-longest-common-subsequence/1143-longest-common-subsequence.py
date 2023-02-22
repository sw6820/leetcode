class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        LCS=[[0]*(len(text2)+1)for _ in range(len(text1)+1)]
        for i,u in enumerate(text1,1):
            for j,v in enumerate(text2,1):
                LCS[i][j]=LCS[i-1][j-1]+1 if u==v else max(LCS[i-1][j],LCS[i][j-1])
        return LCS[-1][-1]