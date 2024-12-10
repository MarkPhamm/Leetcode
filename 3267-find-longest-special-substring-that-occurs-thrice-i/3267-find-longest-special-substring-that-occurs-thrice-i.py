# 1. Initialize `max_length = -1`
# 2. Iterate `length` from len(s) down to 1:
#     a. Create a hash map `substring_count` to count occurrences of substrings
#     b. For `i` from 0 to len(s) - length:
#         i. Extract substring `sub = s[i:i+length]`
#         ii. If `sub` is "special" (all characters are the same):
#             - Increment its count in `substring_count`
#     c. Check `substring_count` for substrings with count >= 3:
#         i. If found, update `max_length` to `length` and break the loop
# 3. Return `max_length`


class Solution:
    def maximumLength(self, s: str) -> int:
        max_length = -1
        for length in range(len(s), 0, -1):  # Start with longest substrings
            substring_count = {}
            for i in range(len(s) - length + 1):  # Generate substrings
                sub = s[i:i + length]
                if len(set(sub)) == 1:  # Ensure the substring is special
                    substring_count[sub] = substring_count.get(sub, 0) + 1
            if any(count >= 3 for count in substring_count.values()):  # Check for validity
                max_length = length
                break
        return max_length




        
        