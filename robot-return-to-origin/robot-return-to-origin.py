class Solution:
    def judgeCircle(self, moves: str) -> bool:
        t=collections.Counter(moves)
        return t['U']==t['D'] and t['L']==t['R']