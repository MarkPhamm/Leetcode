from itertools import accumulate

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", 'e' , 'i' ,'o' ,'u'}

        words_list = []
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                words_list.append(1)
            else:
                words_list.append(0)
        
        prefix = list(accumulate(words_list))
        
        ans = []
        for query in queries:
            if query[0] == 0:
                ans.append(prefix[query[1]])
            else:
                ans.append(prefix[query[1]] - prefix[query[0]-1])
        return ans
        