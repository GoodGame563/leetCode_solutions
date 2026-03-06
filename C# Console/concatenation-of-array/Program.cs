using System;
using System.Collections.Generic;

public class Solution
{
    public int[] GetConcatenation(int[] nums) {
        int n = nums.Length;
        int[] result = new int[n+n];
        for (int i = 0; i < n; i++)(result[i], result[i+n]) = (nums[i],nums[i]);
        return result;
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        
    }
}
