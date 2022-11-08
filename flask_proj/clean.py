millnames = ['Million','Billion','Trillion']

def human_readable(n):
    n = int(n)
    if n >= 1000 and n < 1000000:
        n = "{:,d}".format(n)
    elif n >= 1000000 and n < 1000000000:
        n = f'{round(n / 1000000, 1)} {millnames[0]}'
    elif n >= 1000000000 and n < 1000000000000:
        n = f'{round(n / 1000000000, 1)} {millnames[1]}'
    elif n >= 1000000000000:
        n = f'{round(n / 1000000000000, 1)} {millnames[2]}'
    return n
   