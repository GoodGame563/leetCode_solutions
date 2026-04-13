from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0 
        pref_sum = {0:1}
        curr_sum = 0
        for num in nums:
            curr_sum+= num
            if (curr_sum-goal) in pref_sum:
                count += pref_sum[curr_sum-goal]
            if curr_sum in  pref_sum:
                pref_sum[curr_sum] +=1
            else:
                pref_sum[curr_sum] = 1
        return count
        
print(Solution().numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0))

