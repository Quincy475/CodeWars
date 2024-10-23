//https://www.codewars.com/kata/514b92a657cdc65150000006
public static class Kata
{
  public static int Solution(int value)
  {
    int start =1;
    int sum = 0;

    for(int i = start; i < value; i++){
      if (i % 5 == 0 ||i % 3 == 0){
        sum += i;
      } 
    }
    return sum;
  }
}