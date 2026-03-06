using System;
using System.Collections.Generic;

public class Solution
{
    public int[] Shuffle(int[] nums, int n) {
        int[] result = new int[nums.Length];
        int index = 0;
        for(int i = 0; i < nums.Length/2; i++){
            result[index] = nums[i];
            result[index+1] = nums[i+n];
            index+=2;
        }
        return result;
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        Console.WriteLine(String.Join(" ",solution.Shuffle([1,2,3,4,4,3,2,1], 2)));
    }
}
