using System;
using System.Collections.Generic;

public class Solution
{
    public int MaxFrequencyElements(int[] nums) {
        int ans = 0, max = 0;
        var exs = new Dictionary<int, int>();
        foreach (int n in nums) if(!exs.TryAdd(n, 1)) exs[n] ++;
        foreach (var (key, value) in exs){
            if (value < max) continue;
            if (value > max)
            {
                ans = 0;
                max = value;
            }
            ans+=value;
        }
        return ans;
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        Console.WriteLine(solution.MaxFrequencyElements([1,2,3,4,5]));
        
    }
}
