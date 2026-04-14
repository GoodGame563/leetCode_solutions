class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        total_unique = len(set(nums))
        result = 0
        for left in range(n):
            see = set()
            for right in range(left, n):
                see.add(nums[right])
                if len(see) == total_unique:
                    result+=n-right
                    break
        return result 



print(Solution().countCompleteSubarrays(nums = [1,3,1,2,2]))
