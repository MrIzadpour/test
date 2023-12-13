starNumbers = int(input("Enter your number: "))

for i in range(1, starNumbers + 1):
    print('*' * i)

for i in range(starNumbers-1, 0,-1):
    print("*" * i)