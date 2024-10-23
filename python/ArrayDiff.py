#https://www.codewars.com/kata/523f5d21c841566fde000009
def array_diff(a, b):

    for int in b:
        while int in a:
            a.remove(int)

    return a