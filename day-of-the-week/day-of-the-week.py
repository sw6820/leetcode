class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        w=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        return w[datetime.datetime(year, month, day).weekday()]