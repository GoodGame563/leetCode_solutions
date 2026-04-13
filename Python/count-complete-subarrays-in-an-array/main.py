class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        total_unique = len(set(nums))
        result = 0
        for left in range(n):
            seen = set()
            for right in range(left, n):
                seen.add(nums[right])
                if len(seen) == total_unique:
                    result+=1
        return result 



print(Solution().countCompleteSubarrays(nums = [5,5,5,5]))
