using System;
using System.Collections.Generic;

public class Solution
{
    public int[] SuccessfulPairs(int[] spells, int[] potions, long success) {
        int [] pairs = new int[spells.Length];
        Array.Sort(potions);
        int potionsLenght = potions.Length;
        for(int i = 0; i< spells.Length; i++)
        {
            long minValue = (long)Math.Ceiling((double)(success) / spells[i]);  
            int index = FindFirstGreaterIndexCustom(potions, minValue);
            if (index < potionsLenght)
            {
                pairs[i] = potionsLenght - index;
            }
            else
            {
                pairs[i] = 0;
            }
        }

        return pairs;
        
    }
    public static int FindFirstGreaterIndexCustom(int[] array, long value)
    {
        int left = 0;
        int right = array.Length; 

        while (left < right)
        {
            int mid = left + (right - left) / 2;

            if (array[mid] >= value)
            {
                right = mid;
            
            }
            else
            {
                left = mid + 1;
                
            }
        }

        return left; 
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        Console.WriteLine(String.Join(" ", solution.SuccessfulPairs([3,1,2], [8,5,8], 16)));
    }
}
