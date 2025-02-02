class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        str_list = str.split(s)
        ans = []
        for string in str_list:
            if string.isnumeric():
                if ans and int(string) <= ans[-1]:
                    return False
                ans.append(int(string))
        return True