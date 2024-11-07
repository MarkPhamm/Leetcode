class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort
        count = {}
        # Create a frequency array
        freq = [[] for i in range(len(nums) + 1)]

        # Count the frequency of each element
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Add the elements to the frequency array
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        print("The frequency array is: ", freq)
    
        # Get the k most frequent elements
        res = []
        # Iterate through the frequency array in reverse order
        for i in range(len(freq)-1, 0, -1):
            # Iterate through the elements in the current frequency bucket
            for n in freq[i]:
                # Add the element to the result list
                res.append(n)
                # If we have collected k elements, return the result
                if len(res) == k:
                    return res

