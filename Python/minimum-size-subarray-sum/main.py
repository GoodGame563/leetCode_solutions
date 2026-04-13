from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, target_sum, min_lenght =0, 0, float('inf')
        for i in range(len(nums)):
            target_sum += nums[i]
            while target_sum >= target:
                min_lenght = min(min_lenght, i-left+1)
                target_sum -= nums[left]
                left+=1
        return 0 if min_lenght == float('inf') else min_lenght
    
        
print(Solution().minSubArrayLen(target = 11, nums = [1,2,3,4,5]))
