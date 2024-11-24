class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len([*filter(lambda x:x%3, nums)])