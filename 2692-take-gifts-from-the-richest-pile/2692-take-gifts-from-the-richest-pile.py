class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()
        for i in range(k):
            squareroot = sqrt(gifts[-1])
            gifts.pop()
            gifts.append(floor(squareroot))
            gifts.sort()
        return sum(gifts)