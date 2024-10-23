#https://www.codewars.com/kata/5583090cbe83f4fd8c000051
def digitize(n):

    lst = []
    for element in str(n):
        element = int(element)
        lst.append(element) 

    lst.reverse()
    return lst