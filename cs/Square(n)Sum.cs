//https://www.codewars.com/kata/515e271a311df0350d00000f
public static class Kata
{
  public static int SquareSum(int[] numbers)
  { 
    int total = 0;
    foreach(int number in numbers){
      total += number * number;
    }
return total;  
  }
}