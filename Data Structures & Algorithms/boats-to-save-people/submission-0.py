class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        n = len(people)
        left, right = 0, n-1

        while left <= right:
            if people[left]+people[right] <= limit:
                count += 1
                left += 1
                right -= 1
            elif people[left]+people[right] > limit or people[right] <= limit:
                count += 1
                right -= 1
            # else:
            #     left += 1
            #     right -= 1

        return count 

            
