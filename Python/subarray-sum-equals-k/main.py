from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, cur_sum = 0, 0  
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        for num in nums:
            cur_sum += num
            count += prefix_count[cur_sum - k]
            prefix_count[cur_sum] += 1
        return count

print(Solution().subarraySum([1, 2, 3], 3))
