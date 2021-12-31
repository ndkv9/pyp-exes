string = input("Please type in a word:")
substring = input("Please type in a character:")

index = string.find(substring)

if index != -1:
    string = string[index + len(substring):]
    subindex = string.find(substring)
    if subindex != -1:
        print(
            f"The second occurrence of the substring is at index {subindex + len(substring) + index}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur in the string.")
