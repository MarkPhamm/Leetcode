class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        dq = deque(enumerate(tickets))  # Track (index, tickets_left) to maintain positions
        ans = 0
        print(dq)
        while dq:
            idx, val = dq.popleft()  # Get the front person's index and remaining tickets
            ans += 1  # They take 1 second to buy a ticket

            if val - 1 > 0:
                dq.append((idx, val - 1))  # If they still need tickets, move them to the end

            if idx == k and val - 1 == 0:  # If the target person is done
                break

        return ans