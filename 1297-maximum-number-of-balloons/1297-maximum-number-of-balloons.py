class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {"b":0, "a":0, "n":0, "l":0, "o":0}
        for char in text:
            hashmap[char] = hashmap.get(char,0)+1
        
        return min(hashmap["b"], hashmap["a"], hashmap["n"], hashmap["l"]//2, hashmap["o"]//2)