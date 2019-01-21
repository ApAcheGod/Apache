import random


def coin_flip(n):

    head = 0
    tail = 0
    for i in range(n):
        a = random.randint(0, 1)
        if a == 0:
            head += 1
        else:
            tail += 1

    print("Орёл выпал - {} раз\nРешка выпала - {} раз".format(head,tail))


def main():

    coin_flip(int(input()))


if __name__ == "__main__":
    main()
