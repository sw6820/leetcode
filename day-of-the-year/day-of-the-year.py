class Solution:
    def dayOfYear(self, date: str) -> int:
        d=[*map(int, date.split('-'))]
        month=[31,28,31,30,31,30,31,31,30,31,30,31]
        return sum(month[:d[1]-1])+d[2]+ (1 if d[1]>2 and (not d[0]%400 or d[0]%100 and not d[0]%4) else 0)
        