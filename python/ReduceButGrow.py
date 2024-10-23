#https://www.codewars.com/kata/57f780909f7e8e3183000078
def grow(arr):
    num = 1    

    for x in arr:
        num = num * x
    return num