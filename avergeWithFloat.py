numbers = input("Please enter your numbers and split them with ,: ").split(',')

sum_of_numbers = 0

for i in numbers:
    sum_of_numbers += float(i)

average = sum_of_numbers / len(numbers)

print(format(average, '.3f'))
