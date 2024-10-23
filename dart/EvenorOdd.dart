//https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
String evenOrOdd(int number) {
if((number/2) != (number /2).roundToDouble()){
  return 'Odd';
}
  else{
    return 'Even';
  }
}