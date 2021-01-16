def square_digits(num):
    acum = ''

    for d in str(num):
        acum = acum+str(pow(int(d), 2))

    return int(acum)
