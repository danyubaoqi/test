def sqrt(number):
    x=1
    y=number/2
    while abs(y-x)>1e-6:
        t=y
        x=t
        y=(y+number/y)/2
    return y