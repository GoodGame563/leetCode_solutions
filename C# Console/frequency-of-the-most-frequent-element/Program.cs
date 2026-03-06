using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Reflection.Metadata;

public class Solution
{
    public int MaxFrequency(int[] nums, int k) {
        Array.Sort(nums);
        int len= nums.Length;
        long[] diff = new long[len];
        for (int i = 1; i< len; i++) diff[i] = nums[i]-nums[i-1];
        long[] pref = new long[len];
        for (int i = 1; i< len; i++) pref[i] = diff[i]+pref[i-1];
        Console.WriteLine(String.Join(" ", diff));
        Console.WriteLine(String.Join(" ", pref));
        int l = 1, h = len;
        while(l < h)
        {
            int m = (h-l + 1) /2+l;
            bool possible = IsPossible(nums, diff, pref, m,k);
            Console.WriteLine(possible); 
            if (possible) l = m;
            else h = m-1;
        } 
        return l;
    }
    private bool IsPossible(int[] nums, long[] diff, long[] pref, int freq, int k)
    {
        int len = diff.Length;
        long times = 0;
        for (int i = freq-2; i>=0; i--)
        {
            times += nums[freq-1] - nums[i];
        }
        Console.WriteLine(times);
        long minTimes = times;

        for(int i = freq; i< len; i++)
        {
            times = times- (pref[i-1] - pref[i-freq])+ diff[i]* (freq-1);
            minTimes = Math.Min(minTimes, times);
        }
        return minTimes <= k;
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        Console.WriteLine(solution.MaxFrequency([9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966], 3056));
    }
}
