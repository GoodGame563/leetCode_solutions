from random import randint
class Solution:
    def quick_select(self, nums: list[int], k:int)->int:
        pivot = nums[randint(0, len(nums)-1)]
        lows, pivots, highs = [], [], []
        for el in nums:
            if el > pivot:
                highs.append(el)
            elif el == pivot:
                pivots.append(el)
            else:
                lows.append(el)
        l_highs, l_pivots = len(highs), len(pivots)
        if k < l_highs:
            return self.quick_select(highs, k)
        elif k < l_highs+ l_pivots:
            return pivots[0]
        else:
            return self.quick_select(lows, k-l_highs-l_pivots)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.quick_select(nums, k-1)


print(Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2))