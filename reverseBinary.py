number = int(input("Enter your decimal number for convert to binary:    "))

binary = ""

while number > 0:
    binary += str(number % 2)
    number = number // 2

print(binary)

count = len(binary) - 1
final_number = 0

for i in binary:
    if int(i) == 1:
        final_number += 2**count
    count -= 1

print(final_number)