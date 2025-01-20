class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        word_set = set(words)
        for word in word_set:
            for other_word in word_set:
                if word in other_word and word!= other_word and word not in ans:
                    ans.append(word)
        return ans
