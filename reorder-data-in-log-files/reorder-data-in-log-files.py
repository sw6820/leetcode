class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l,d=[],[]
        for i in logs:
            if i.split()[1].isnumeric():d.append(i)
            else: l.append(i)                                            
        return sorted(l, key=lambda x:[x.split()[1:],x.split()[0]])+d