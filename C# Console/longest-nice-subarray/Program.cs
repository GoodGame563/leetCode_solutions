using System;
using System.Collections.Generic;
using System.Xml.XPath;

public class Solution
{
    public int LongestNiceSubarray(int[] nums) {
        int ans = 0;
        int used = 0;
        for (int left = 0, right = 0; right < nums.Length; right++)
        {
            while((used & nums[right]) != 0){
                used ^= nums[left];
                left++;
            }
            used |= nums[right];
            ans = Math.Max(ans, right-left+1);
        }
        return ans;
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        Console.WriteLine(solution.LongestNiceSubarray([1,3,8,48,10]));
    }
}
