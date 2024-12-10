class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        queue = []


        for i in range(len(s)):
            # Update character count
            counter[s[i]] = counter.get(s[i], 0) + 1
            # Enqueue the index
            queue.append(i)
            # Remove invalid elements from the queue
            while queue and counter[s[queue[0]]] > 1:
                queue.pop(0)

        return queue[0] if queue else -1