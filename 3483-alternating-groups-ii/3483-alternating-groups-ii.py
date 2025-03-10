class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

    
        # Extend the array to handle circular sequences
        for i in range(k - 1):
            colors.append(colors[i])

        n = len(colors)
        l, r = 0 , 1
        result = 0

        while r < n:
            # check if current color is same as the last one:
            if colors[r] == colors[r - 1]:
                # pattern breaks, reset window
                l = r
                r +=1
                continue
            
            # extend window:
            r +=1
            
            # skip counting if current length < k
            if r - l < k:
                continue
            
            result +=1
            l+=1
        return result