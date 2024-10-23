#https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
def open_or_senior(data):
    x = 0    
    while len(data) > x:
        if data[x][0] >= 55 and data[x][1] > 7:
            data[x] = "Senior"
        else:           
            data[x] = "Open"
        x += 1
    return data