class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank_dict = dict(zip(sorted_arr, range(1,len(sorted_arr)+1)))

        return [rank_dict[num] for num in arr]
