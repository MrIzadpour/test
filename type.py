#  Solution 1

# def input_type_list(inp_list):
#     type_identifier = lambda inp_list:[type(item) for item in inp_list]
#     return type_identifier(inp_list)

# print(input_type_list([1, (2, 5, 6), 120.256, True, "Hi", [1, 2, 3], {1:25}]))  

# Solution 2

list_1 = [1, (2, 5, 6), 120.256, True, "Hi", [1, 2, 3], {1:25}]
list_2 = list(map(lambda x: type(x), list_1))
print(list_2)
