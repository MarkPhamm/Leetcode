class Solution:
    def countAsterisks(self, s: str) -> int:
        split_list = s.split('|')
        str_ans = ""
        for i in range(len(split_list)):
            if i%2 == 0:
                str_ans += split_list[i]
        return str_ans.count("*")       