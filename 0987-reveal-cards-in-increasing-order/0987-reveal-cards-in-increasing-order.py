class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # [2,13,3,11,5,17,7]
        # [3,11,5,17,7,13] 2
        # [5,17,7,13,11] 3
        # [7,13,11,17] 5
        # [11,17,13] 7
        # [13,17] 11
        # [17], 13
        # [] 17
        # Built from the bottom up
        # [17]
        # [13,17]
        # [11,17,13]
        # [7,13,11,17]
        # [5,17,7,13,11]
        # [3,11,5,17,7,13]
        # [2,13,3,11,5,17,7]

        deck.sort(reverse=True)
        ans = deque() 
        ans.append(deck[0])
        for num in deck[1:]:
            ans.appendleft(ans.pop())
            ans.appendleft(num)
        
        return list(ans)
            


