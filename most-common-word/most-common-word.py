
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:                
        return collections.Counter(w for w in re.findall(r'\w+', paragraph.lower()) if w not in set(banned)).most_common(1)[0][0]