import random as R

# guess = R.randint(1, 99)

# print(guess)

# answer = input("If is true write D, If is greater write B and If is less write K:   ")
# new_guess = guess 
# min = 1 
# max = 99

# while answer.lower() != "d":
#     answer = input("If is true write D, If is greater write B and If is less write K:   ")
#     if answer.lower() == "k":
#         max = new_guess - 1
#         new_guess = R.randint(min, max)
#         print(new_guess)
#     elif answer.lower() == "b":
#         min = new_guess - 1
#         new_guess = R.randint(min, max)
#         print(new_guess)
#     elif answer == "d":
#         d = "d"


guess = R.randint(1, 99)
print(guess)
d = 's'
new_guess = guess
min = 1 
max = 99
while d != 'd':
    our_input = input('If is true write D, If is greater write B and If is less write K:   ')
    if our_input == 'k':
        max = new_guess - 1
        new_guess = R.randint(min, max)
        print(new_guess)
    elif our_input == 'b':
        min = new_guess + 1
        new_guess = R.randint(min, max)
        print(new_guess)
    elif our_input == 'd':
        d = 'd'

print('my guess finally is true ...')