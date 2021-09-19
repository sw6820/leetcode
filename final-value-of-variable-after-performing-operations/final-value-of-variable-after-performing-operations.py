class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        c=collections.Counter(operations)
        return c['++X']+c['X++']-c['X--']-c['--X']