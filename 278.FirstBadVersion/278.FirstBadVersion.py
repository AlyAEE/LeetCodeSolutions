class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1 or isBadVersion(1) == True:
            return 1
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid) == False:
                low = mid + 1
            elif isBadVersion(mid) == True:
                high = mid -1
        return low