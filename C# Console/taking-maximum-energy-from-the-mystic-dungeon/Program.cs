using System;
using System.Collections.Generic;

public class Solution
{
    public int MaximumEnergy(int[] energy, int k) {
        Array.Reverse(energy);
        for(int i = k; i< energy.Length; i += 1)
        {
            energy[i] += energy[i-k];    
        }
        return energy.Max();
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        Console.WriteLine(solution.MaximumEnergy([-2,-3,-1], 2));
        
    }
}
