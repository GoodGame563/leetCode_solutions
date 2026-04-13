from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cur_sum = 0
        see = {0:-1}
        for i, x in enumerate(nums):
            cur_sum+=x
            mod = cur_sum % k
            if not mod in see:
                see[mod] = i 
                continue
            if i - see[mod] >=2:
                return True 
        return False


print(Solution().checkSubarraySum(nums = [5,0,0,0], k = 3))

print(0%3,6%6)
print((25+6)%6)