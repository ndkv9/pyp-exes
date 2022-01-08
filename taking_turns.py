number = int(input("Please type in a number:"))
i = 1

while i <= number:
    if i == number:
        print(i)
        i += 1
        number -= 1
    else:
        print(i)
        print(number)
        i += 1
        number -= 1
