numbers = []
while True:
    number = input("Enter a number: ")
    if number == "":
        break

    numbers.append(float(number))
numbers = sorted(numbers, reverse=True)
print("Five greatest numbers:")
for i in range(min(5, len(numbers))):
    print(numbers[i])

