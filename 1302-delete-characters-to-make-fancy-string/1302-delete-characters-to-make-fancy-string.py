class Solution:
    def makeFancyString(self, s: str) -> str:
        has_two = False
        prev = None
        result = []
        for x in s:
            if prev == x:
                if not has_two:
                    result.append(x)
                    has_two = True
            else:
                result.append(x)
                prev = x
                has_two = False
        return ''.join(result)