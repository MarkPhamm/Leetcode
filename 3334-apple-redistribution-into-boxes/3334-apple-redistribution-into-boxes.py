class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse = True)
        ans = 0
        for c in capacity:
            if total <= 0:
                break
            ans += 1
            total -= c
        return ans
