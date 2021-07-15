class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rst=[]
        a=['qwertyuiop','asdfghjkl','zxcvbnm']
        for w in words:
            t=[]
            for i in w.lower():
                if i in a[0]: t.append(0)
                elif i in a[1]: t.append(1)
                else: t.append(2)
            if len(set(t))==1:rst.append(w)
        return rst