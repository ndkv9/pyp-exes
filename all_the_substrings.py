word = input("Please type in a word:")
char = input("Please type in a character:")

while True:
    index = word.find(char)
    if len(word) < 3 or index < 0 or index + 3 > len(word):
        break

    print(word[index : index + 3])

    word = word[index + 1 :]
