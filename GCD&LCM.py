# print("Enter Two Numbers: ")
# numOne = int(input())
# numTwo = int(input())
#
# if numOne>numTwo:
#     lcm = numOne
# else:
#     lcm = numTwo
#
# while True:
#     if lcm%numOne==0 and lcm%numTwo==0:
#         break
#     else:
#         lcm = lcm + 1
#
# gcd = (numOne * numTwo) / lcm
# print("\nLCM =", lcm)
# print("\nGCD =", gcd)

#           Second Solution
#
# number1 = int(input("please enter your input: "))
# number2 = int(input("please enter your input: "))
#
# Max, Min, lcm, gcd = 0, 0, 0, 0
#
# if number1 > number2:
#     Max = number1
#     Min = number2
#
# if number2 > number1:
#     Max = number2
#     Min = number1
#
# if number1 == number2:
#     Max = number1
#     Min = number2
#
# remind = Max % Min
#
# if remind == 0:
#     gcd = Max
#     lcm = Min
#
# else:
#     for i in range(1, Max):
#         if i <= Min:
#             if Max % i == 0 and Min % i == 0:
#                 gcd = i
#
#     lcm = (Max * Min) / gcd
#
# print("GCD is: ", gcd)
# print("LCM is: ", lcm)


#           Third Solution(راه حل اقلیدسی)

number1, number2 = map(int, input("Enter your number: ").split(','))

number1main, number2main = number1, number2

if number1 < number2:
    number1, number2 = number2, number1

while number2 != 0:
    remaining = number1 % number2
    number1 = number2
    number2 = remaining

GCD = number1
LCM = (number1main * number2main) / GCD

print("GCD is: ", GCD)
print("LCM is: ", LCM)