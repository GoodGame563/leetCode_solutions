using System;
using System.Collections.Generic;

public class Solution
{
    public IList<int> FindLonely(int[] nums) {
        List<int> ans = new List<int>(nums.Length);
        int [] ex = new int [nums.Max()+2];
        foreach(int n in nums) for (int i = -1; i <= 1; i++) {
            if(n+i < 0) continue;
            ex[n+i] += 1;
        }
        foreach(int n in nums) if(ex[n]<2) ans.Add(n);
        return ans;
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        Console.WriteLine(String.Join(" ",solution.FindLonely([61,83,92,92,42,60,16,45,32,14,40,7,10,34,62,33,65,79,7,14,85,21,36,5,99,25,0,14,52,41,40])));
    }
}
