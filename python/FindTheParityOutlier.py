#https://www.codewars.com/kata/5526fc09a1bbd946250002dc
def find_outlier(integers):
    odd = []
    even = []

    for int in integers:
        even.append(int) if (int % 2) == 0 else odd.append(int)

    return even[0] if len(even) == 1 else odd[0] 