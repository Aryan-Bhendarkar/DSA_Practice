class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = dict()
        ans = list()
        for a in nums:
            hashmap[a] = hashmap.get(a, 0) + 1

        for key, val in hashmap.items():
            if val > len(nums)//3:
                ans.append(key)

        return ans 
