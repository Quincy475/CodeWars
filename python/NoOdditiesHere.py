#https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce
def no_odds(values): 
    x=0
    while len(values) > x:
        if (values[x] % 2) == 0:
            x +=1
        else: 
            del values[x]

    return values