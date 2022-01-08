def line(amount, string):
    if len(string) == 0:
        print("*" * amount)
    else:
        print(string[0] * amount)


def spruce(height):
    i = 1
    amount = 1

    print("a spruce!")

    while i <= height:
        print((height - i) * " ", end="")
        line(amount, "*")
        i += 1
        amount += 2

    print(" " * (height - 1), end="")
    line(1, "*")
