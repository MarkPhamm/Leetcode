class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in digits:
            string += str(i)
        new_string = str(int(string)+1)

        results = []
        for i in new_string:
            results.append(int(i))
        
        return results

        