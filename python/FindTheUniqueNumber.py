#https://www.codewars.com/kata/585d7d5adb20cf33cb000235
def find_uniq(arr):
    
    arr.sort()

    return arr[0] if arr[0] != arr[1] else arr[len(arr) -1]   