class Solution:
    def sortColors(self, nums: list[int]) -> None:
        left, center, right = [],[],[]
        while len(nums) > 0:
            match nums.pop():
                case 0:
                    left.append(0)
                case 1:
                    center.append(1)
                case 2:
                    right.append(2)
        nums.extend(left)
        nums.extend(center)
        nums.extend(right)
            
nums = [2,0,2,1,1,0]
print(Solution().sortColors(nums))
print(nums)
