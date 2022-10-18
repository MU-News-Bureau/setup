millnames = [' Million',' Billion',' Trillion']

def human_readable(n):
    if n >= 1000000 and n < 1000000000:
        n = f'{n / 1000000} {millnames[0]}'
    elif n >= 1000000000 and n < 1000000000000:
        n = f'{n / 1000000000} {millnames[1]}'
    elif n >= 1000000000000:
        n = f'{n / 1000000000000} {millnames[2]}'
    print(n)
    



