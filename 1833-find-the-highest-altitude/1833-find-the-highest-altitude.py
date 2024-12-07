class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0]
        attitudes = 0
        for g in gain:
            current = prefix[-1] + g
            attitudes = max(current, attitudes)
            prefix.append(current)
        print(prefix)
        return attitudes