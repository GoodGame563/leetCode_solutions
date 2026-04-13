from typing import List
from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [1 if num == 1 else -1 for num in nums]
        count = 0   
        prefix_sum = 0
        prefix_sum_count = {0: -1}  
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum in prefix_sum_count:
                count = max(count, i - prefix_sum_count[prefix_sum])
            else:
                prefix_sum_count[prefix_sum] = i
        return count

print(Solution().findMaxLength([0,1,1,1,1,1,0,0,0]))

