class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        print(start,destination)
        return min(sum(distance[min(start,destination):max(start,destination)]),sum(distance)-sum(distance[min(start,destination):max(start,destination)]))