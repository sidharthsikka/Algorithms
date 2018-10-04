def swap_with_temp(x,y):
    temp = x
    x = y
    y = temp

def swap_without_temp(x,y):
    x += y
    y = x - y
    x = x - y