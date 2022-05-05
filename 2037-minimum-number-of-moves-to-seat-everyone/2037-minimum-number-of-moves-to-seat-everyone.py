class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(t-s) for s,t in zip(sorted(seats), sorted(students)))