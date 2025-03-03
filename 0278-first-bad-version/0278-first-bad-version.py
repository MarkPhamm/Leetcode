# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n

        while l <= r:
            mid = (l+r)//2
            if isBadVersion(mid) and not isBadVersion(mid-1): # if mid version is bad, mid version - 1 is not bad
                return mid
            elif isBadVersion(mid): # if mid version is bad, search for previous version
                r = mid - 1 
            elif not isBadVersion(mid): # if mid version is good, search version after
                l = mid + 1
        