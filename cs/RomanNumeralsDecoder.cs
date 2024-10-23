//https://www.codewars.com/kata/51b6249c4612257ac0000005
using System;
using System.Collections.Generic;

public class RomanDecode
{
	public static int Solution(string roman)
	{
     Dictionary<char, int> romanNumerals = new Dictionary<char, int>
        {
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 }
        };
  char[] charArray = roman.ToCharArray();
    Console.WriteLine(charArray);
    
    int total = 0;
        int previousValue = 0;

        for (int i = roman.Length - 1; i >= 0; i--)
        {
            int currentValue = romanNumerals[roman[i]];

            if (currentValue < previousValue)
            {
                total -= currentValue;
            }
            else
            {
                total += currentValue;
            }

            previousValue = currentValue;
          }
    return total;
  }
}