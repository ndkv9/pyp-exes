

while True:
    number = int(input("Please type in a number:"))
    if number <= 0:
        print("Thanks and bye!")
        break
    factorial = 1
    irator = number
    while irator >= 1:
        factorial *= irator
        irator -= 1
    print(f"The factorial of the number {number} is {factorial}")
