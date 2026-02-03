class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        delta_change = (sumA - sumB)/2
        set_B = set(bobSizes) 

        for c in aliceSizes:
            if c - delta_change in set_B:
                return [c, c - delta_change]