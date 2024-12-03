class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string_list = []
        prev = 0
        for space in spaces:
            string_list.append(s[prev:space])
            prev = space
        string_list.append(s[prev:])
        print(string_list)

        return ' '.join(string_list)

        