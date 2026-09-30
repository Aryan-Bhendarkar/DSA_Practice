class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_element = max(piles)

        def finding_time(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time 

        l, r = 1, max_element
        while l <= r:
            mid = (l + r) //2
            if finding_time(mid) <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l
