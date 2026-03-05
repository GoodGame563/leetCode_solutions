using System;
using System.Collections.Generic;
using System.Formats.Asn1;

public class Solution
{
    public int[] AvoidFlood(int[] rains) {
        int[] ans = new int[rains.Length];
        Dictionary<int,int> lakeFullDays = new();
        LinkedList<int> skip_index = new();
        for(int i = 0; i < rains.Length; i++)
        {
            int value= rains[i];
            if (value == 0) {
                skip_index.AddLast(i);
                ans[i] = 1;
                continue;
            }
            if(lakeFullDays.TryGetValue(value, out int index))
            {
                var isDry = false;
                foreach(var dryDay in skip_index)
                {
                    if(dryDay > index)
                    {
                        ans[dryDay] = value;
                        skip_index.Remove(dryDay);
                        isDry = true;
                        break;
                    }
                }
                if(!isDry)
                {
                    return [];
                }
            }
            lakeFullDays[value] = i;
            ans[i] = -1;
        }
        return ans;
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        // int[] rains = [1,2,0,1,2];
        // int[] rains = [1,0,2,3,0,1,2];
        int[] rains = [1,0,2,0,2,1];
        Console.WriteLine(String.Join(' ', solution.AvoidFlood(rains)));
    }
}
