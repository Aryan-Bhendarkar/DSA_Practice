class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curr_sum = 0
        prefixsum = {0: 1}

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            res += prefixsum.get(diff, 0)
            prefixsum[curr_sum] = prefixsum.get(curr_sum, 0) + 1

        return res