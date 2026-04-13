from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        final = 0
        count = {0: 1}
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod in count:
                final += count[mod]
                count[mod] += 1
            else:
                count[mod] = 1 
        return final 
    
print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))


