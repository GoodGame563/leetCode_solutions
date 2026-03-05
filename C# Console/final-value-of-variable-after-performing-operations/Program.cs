using System;
using System.Collections.Generic;
using System.Security.Cryptography;

public class Solution {
    public int FinalValueAfterOperations(string[] operations) {
        int x = 0;
        foreach(string s in operations)
        {
            if (s[1] == '+') x++;
            else x--;
            
        }
        return x;
        
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        Console.WriteLine(solution.FinalValueAfterOperations(["--X","X++","X++"]));
    }
}
