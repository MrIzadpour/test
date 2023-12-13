#   # راه حل اول برای مقسوم علیه اول

# n = int(input("Enter the number for calculating the prime factors :\n"))
# for i in range(2, n + 1):
#     if n % i == 0:
#         count = 1
#         for j in range(2, (i//2 + 1)):
#             if i % j == 0:
#                 count = 0
#                 break
#         if count == 1:
#             print(i)


# گرفتن ورودی

Number = int(input("Please Enter Your Number: "))

# اولین حلقه برای پیدا کردن مقوسم علیه ها

for i in range(2, Number):
    if Number % i == 0:
        count = 1

# دومین حلقه برای پیدا کردن مقسوم علیه های اول

        for j in range(2, i-1):
            if i % j == 0:
                break
        else:
            print(i,end=' ')