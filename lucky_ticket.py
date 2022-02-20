# Save the input in this variable
ticket = input()

# Add up the digits for each half
list1 = []
for i in (ticket[:(len(ticket)//2)]):
    i = int(i)
    list1.append(i)

list2 = []
for i in (ticket[(len(ticket)//2):]):
    i = int(i)
    list2.append(i)

half1 = sum(list1)
half2 = sum(list2)

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
