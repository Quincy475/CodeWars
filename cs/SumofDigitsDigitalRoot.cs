// https://www.codewars.com/kata/541c8630095125aba6000c00
using System;
public class Number
{
  public static int DigitalRoot(long n)
  {
    int sum = 0;

    while (n > 0 || sum > 9)
    {
        if (n == 0)
        {
            n = sum;
            sum = 0; 
        }

        sum += (int)(n % 10);
        n /= 10;
    }

    return sum;

}
}