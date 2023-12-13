n = int(input("Please Insert Your number: "))

fib = [0, 1]

count = 0

for items in range(1, n):
    fib_num = fib[items] + fib[count]
    fib.append(fib_num)
    count += 1
print(fib)

# # راه حل دوم برای حل فیبوناچی


# Enter number of terms needed                   #0,1,1,2,3,5....
# a = int(input("Enter the terms: "))
# f = 0                                         #first element of series
# s = 1                                         #second element of series
# if a <= 0:
#     print("The requested series is", f)
# else:
#     print(f, end=" ")
#     for x in range(2, a):
#         b = f+s
#         print(b, end=" ")
#         f = s
#         s = b
