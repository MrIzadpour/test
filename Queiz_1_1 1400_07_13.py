# 1.A
s = input("Enter the problem: ")
print("Result:", eval(s))


# 1.B
def shift(li: list, i: int) -> list:
    i %= len(li)
    return li[i:] + li[:i]


li = [0, 1, 2, 3, 4]
i = int(input("Enter your shift number:     "))

print(shift(li, i))

# 1.C
# l1, l2 = [1, 2, 3, 4], [2, 6, 3, 2]
# res1 = [x*y for x,y in zip(l1, l2)]  # Solution 1
list_1 = input("enter your input:   ").split(" ")
list_2 = input("enter your input:   ").split(" ")

list_1 = list(map(int, list_1))
list_2 = list(map(int, list_2))

# list_1 = [1, 2, 3]
# list_2 = [3, 4, 5]

if len(list_1) == len(list_2):
    list_3 = list(zip(list_1, list_2))
    print(list_3)
    list_4 = list(map(lambda x: x[0] * x[1], list_3))
    print(list_4)
else:
    print("Your list is not equal")
