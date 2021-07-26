class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        rst=[]
        d=[0]*(n+1)
        for i in target:
            d[i]=1
        for i in range(1,n+1):
            rst.append('Push')
            if i==target[-1]:return rst
            if not d[i]: rst.append('Pop')
        return rst
            