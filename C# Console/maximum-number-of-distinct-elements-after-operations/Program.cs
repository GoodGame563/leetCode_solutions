using System;
using System.Collections.Generic;

public class Solution
{
    public int MaxDistinctElements(int[] nums, int k) {
        Array.Sort(nums);
        int cnt = 0;
        int prev = int.MinValue;
        Console.WriteLine(String.Join(" ",nums));
        Console.WriteLine($"cnt: {cnt} prev: {prev}");

        foreach(int num in nums){
            int curr = Math.Min(Math.Max(num - k, prev + 1), num + k);
            if (curr > prev)
            {
                cnt++;
                prev = curr;
            }
            Console.WriteLine($"curr: {curr} cnt: {cnt} prev: {prev}");
        }
        return cnt;
    }   
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        solution.MaxDistinctElements([4,4,4,4], 2);
    }
}
