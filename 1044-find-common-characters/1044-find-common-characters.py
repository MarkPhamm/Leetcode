class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for char in words[0]:
            benchmark = []
            for i in range(1,len(words)):
                if char in words[i]:
                    benchmark.append(True)
                    words[i] = words[i].replace(char,"",1)
                else:
                    benchmark.append(False)
            if False in benchmark:
                pass
            else:
                ans.append(char)
        return ans

            

        