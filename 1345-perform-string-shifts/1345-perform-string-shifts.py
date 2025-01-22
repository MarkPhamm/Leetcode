class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def shift_func(s, direction, amount):
            amount %= len(s)
            if direction == 0:
                s = s[amount:] + s[:amount]
            elif direction == 1: 
                s = s[-amount:] + s[:-amount]
            return s
        for direction, amount in shift:
            s = shift_func(s, direction, amount)
            print(s)
        return s