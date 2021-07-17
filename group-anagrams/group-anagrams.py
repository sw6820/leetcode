class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        dic=collections.defaultdict(list)
        for w in strs:
            dic[''.join(sorted(w))].append(w)
        return dic.values()
        