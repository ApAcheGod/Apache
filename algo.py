def algo(n):

    counter = 0
    while n != 1:
        if n % 2 == 0:
            counter += 1
            n = n / 2
            algo(n)
        else:
            counter += 1
            n = n * 3 + 1
            algo(n)
    return counter

print(algo(int(input())))
