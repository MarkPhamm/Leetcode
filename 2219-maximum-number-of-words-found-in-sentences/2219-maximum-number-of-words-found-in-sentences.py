class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count_space = sentences[0].count(" ")
        for sentence in sentences:
            count_space = max(count_space, sentence.count(" "))

        return count_space + 1