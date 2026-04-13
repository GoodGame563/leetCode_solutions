from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod =10**9 +7
        result, prefix = 0, 0 
        odd, even = 0, 1
        for num in arr:
            prefix = (prefix+num)%2
            if prefix == 0:
                result += odd
                even+=1
            else:
                result += even
                odd+=1
        return result % mod
    
print(Solution().numOfSubarrays([1,3,5]))
    


        

