number = input("Enter a number: ")
num_digits = 0
index = 0

while index < len(number):
    if number[index].isdigit():
        num_digits += 1
        index += 1
print(num_digits)