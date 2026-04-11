from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        lenght = len(nums)
        if lenght == 1:
            return 1 if nums[0] == k else 0
        for i in range(1, lenght): 
            nums[i] += nums[i-1]
        left = 0 
        result = 0
        for right in range(1, lenght):
            while left < right and nums[right] - nums[left] > k:
                left += 1
            if nums[right] - nums[left] == k:
                result += 1


        return result + 1


print(Solution().subarraySum([1], 0))
