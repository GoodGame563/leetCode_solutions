using System;
using System.Collections.Generic;

public class Solution
{
    public int FindSmallestInteger(int[] nums, int value) {
        var resList = new int[value];
        for(var i = 0; i < nums.Length; i++){
            var num = nums[i] % value;
            num = num < 0 ? num + value : num;
            resList[num] = resList[num] + 1;
        }
        var minValue = int.MaxValue;
        var minIndex = 0;
        for(var i = 0; i < value; i++){
            if(resList[i] < minValue){
                minValue = resList[i];
                minIndex = i;
            }
        }

        return minValue * value + minIndex;
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        solution.FindSmallestInteger([1,-10,7,13,6,8], 7);
    }
}
