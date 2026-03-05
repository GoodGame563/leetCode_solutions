using System;
using System.Collections;
using System.Collections.Generic;

public class Solution
{
    public long MaximumTotalDamage(int[] power) {
        var freq = new Dictionary<int, long>();
        foreach (var p in power) {
            if (!freq.ContainsKey(p)) freq[p] = 0;
            freq[p]++;
        }
        var keys = freq.Keys.ToList();
        Console.WriteLine(String.Join(" ",freq));

        keys.Sort();
        int n = keys.Count;
        long[] dp = new long[n];
        dp[0] = freq[keys[0]] * keys[0];
        Console.WriteLine(String.Join(" ",dp));

        for (int i = 1; i < n; i++) {
            long take = freq[keys[i]] * keys[i];
            int l = 0, r = i - 1, ans = -1;
            while (l <= r) {
                int mid = (l + r) / 2;
                if (keys[mid] <= keys[i] - 3) { ans = mid; l = mid + 1; }
                else r = mid - 1;
            }
            if (ans >= 0) take += dp[ans];
            dp[i] = Math.Max(dp[i - 1], take);
            Console.WriteLine(String.Join(" ",dp));
        }
        return dp[n - 1];
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        Console.WriteLine(solution.MaximumTotalDamage([5,9,2,10,2,7,10,9,3,8]));
    }
}
