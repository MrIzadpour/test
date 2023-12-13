# likes = {"color": 40 , "fruit": 15.25, "pet": 25}
#
# for like in likes.copy():
#     if likes[like] >= 20:
#         del likes[like]
#
# print(likes)


# numbers = {"one": 1, "two": 2, "three": 3, "four": 4}
#
# small_numbers = {}
#
# for key, value in numbers.items():
#     if value <= 2:
#         small_numbers[key] = value
#         print(small_numbers[key])
#         print(value)
#
# print(small_numbers)

#
# incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}
# print(sum(incomes.values()))
# total = 0

# for income in incomes.values():
#     total += income

# swapped = {}
# for key,value in incomes.items():
#     swapped[value] = key
#
# print(swapped)
#
#
# categories = ["color", "fruit", "pet"]
# objects = ["blue", "apple", "dog"]
# print(dict(zip(categories, objects)))
#
# likes = {key: value for key, value in zip(categories, objects)}
#
# print(likes)

# incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}
#
# for fruit, income in sorted(incomes.items(), key=lambda item: item[1]):
#     print(fruit, "->", income)
#
#
# sorted(cities, key= lambda city: city['population'])


# cars = [
#     {
#         "name": "pride",
#         "color": "abi",
#     },
#     {
#         "name": "samand",
#         "color": "sefid"
#     },
#     {
#         "name": "benz",
#         "color": "meshki"
#     }
# ]
#
# cars = sorted(cars, key=lambda car: car['name'])
# print(cars.keys(), "->",cars[color])
# import item as item
#
# incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}
#
# # newInacomes = {fruit: incomes[fruit] for fruit in sorted(incomes)}
#
# newIncomes1 = {fruit: income for fruit, income in sorted(incomes.items(), key=lambda item: item[1], reverse=True)}
#
# print(newIncomes1)


# likes = {"color": "purple", "fruit": "strawberry", "pet": "monkey"}
#
# while True:
#     try:
#         print(f"Dictionary length: {len(likes)}")
#         item = likes.popitem()
#         print(f"item {item} removed")
#
#     except KeyError:
#         print("Your dictionary is empty")
#         break


# fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}
#
#
# def apply_discount(product, discount=0.05):
#     return product[0], round(product[1] * (1 - discount), 2)
#
#
# print(dict(map(apply_discount, fruits.items())))
# print(dict(map(lambda item: apply_discount(item, 0.1), fruits.items())))


# def has_low_price(item, price=0.4):
#     return item[1] < price
#
#
# dict(filter(has_low_price, fruits.items()))
# print(dict(filter(lambda item: has_low_price(item, 0.4), fruits.items())))

from collections import ChainMap

for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
pets = ChainMap(for_adoption, vet_treatment)

for pet, count in pets.items():
    print(pet, "->", count)