class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l=len(list1)+len(list2)
        t=[[]for _ in range(l)]
        a,b={s:i for i,s in enumerate(list1)},{s:i for i,s in enumerate(list2)}
        for i in list1:
            if i in list2:
                t[a[i]+b[i]].append(i)
        for i in t:
            if i: return i