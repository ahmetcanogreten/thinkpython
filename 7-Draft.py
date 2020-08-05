


def find_square_root(x):
    yp = x
    while True:
        y = (yp + (x/yp))/2
        if yp == y:
            break
        yp = y        
    return y

print(find_square_root(16))
