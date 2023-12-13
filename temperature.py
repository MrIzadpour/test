def t_convert(temp):
    far = (temp * 1.8) + 32
    return far

# temp = float(input("Please tell us a C degrees which is gonna convert to F :  "))
list_1 = [1, 2, 3, 4, 5, 6]
list_2 = list(map(t_convert, list_1))
print(list_2)