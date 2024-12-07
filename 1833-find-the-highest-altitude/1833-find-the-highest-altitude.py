class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0]
        for g in gain:
            prefix.append(prefix[-1] + g)
        return max(prefix)