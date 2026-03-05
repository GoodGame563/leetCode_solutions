using System;
using System.Collections.Generic;

public class Solution
{
    public int MaxIncreasingSubarrays(IList<int> nums) {
        int n = nums.Count;
        int cnt = 1, precnt = 0, ans = 0;
        for (int i = 1; i < n; ++i)
        {
            if (nums[i] > nums[i - 1])
            {
                ++cnt;
            }
            else
            {
                precnt = cnt;
                cnt = 1;
            }
            ans = Math.Max(ans, Math.Min(precnt, cnt));
            ans = Math.Max(ans, cnt / 2);
        }
        return ans;
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        solution.MaxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]);
    }
}
