using System;
using System.Collections.Generic;

public class Solution
{
    public IList<string> RemoveAnagrams(string[] words) {
        List<string> result = new();
        result.Add(words[0]);
        for (int i = 1; i< words.Length; i++)
        {
            if(!AreAnagram(words[i-1], words[i]))
            {
                result.Add(words[i]);
            }
        }
        return result;
    }
    bool AreAnagram(string firstWord, string secondWord)
    {
        if (firstWord == secondWord) return true;
        if(firstWord.Length != secondWord.Length) return false;
        int[] characterMap = new int[26];
        for (int index = 0; index < firstWord.Length; index++)
            characterMap[firstWord[index] - 'a']++;
        
        for (int index = 0; index < secondWord.Length; index++)
            if (--characterMap[secondWord[index] - 'a'] < 0)
                return false;
        return true;
    }
}

class Program
{
    static void Main(string[] args)
    {
        var solution = new Solution();
        Console.WriteLine(String.Join(" ",solution.RemoveAnagrams(["abba","baba","bbaa","cd","cd"])));
    }
}
