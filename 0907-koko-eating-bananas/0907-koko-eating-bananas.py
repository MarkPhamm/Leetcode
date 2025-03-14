class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1 , max(piles)
        ans = r
        while l <= r:
            mid = (l+r)//2
            cur_h = sum(ceil(p / mid) for p in piles)

            if cur_h <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        