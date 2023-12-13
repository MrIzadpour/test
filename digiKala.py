# First Solution

# def digikala(num):
#     final_1 = []
#     a = True
#     while True:
#         if final_1 == []:
#             num_1 = [j for i,j in enumerate(num) if j not in num[:i]]
#             rep = []
#             for i in num_1:
#                 if num.count(i) > 1:
#                     rep.append(num.count(i))
#             string = "".join(num_1) + "".join(list(map(str, rep)))
#             string = sorted(list(map(int, list(string))))
#             string = "".join(map(str, string))
#             final_1.append(string)
#         else:
#             num = final_1[-1]
#             num_1 = [j for i,j in enumerate(num) if j not in num[:i]]
#             rep = []
#             for i in num_1:
#                 if num.count(i) > 1:
#                     rep.append(num.count(i))
#             string = "".join(num_1) + "".join(list(map(str, rep)))
#             string = sorted(list(map(int, list(string))))
#             string = "".join(map(str, string))
#             final_1.append(string)
#             a = num != string
#     return final_1[-1]
# print(digikala(list(input("Enter your number:   "))))

# Second Solution

def compression(user_input):
    if isinstance(user_input, str) and user_input.isdigit() and 1 <= len(user_input) <= 1000:
        not_compressed = user_input
        while True:
            number_of_repetition = {}
            # Delete duplicate elements by sets
            compressed_text = list(set(not_compressed))
            # Calculte number of repetition for each elements
            for i in not_compressed:
                number_of_repetition[i] = str(not_compressed.count(i))
            # Add number of repetition to end of string if is greater than 2
            for i in number_of_repetition.values():
                if int(i) >= 2:
                    compressed_text.append(i)
            # Ascending sort
            compressed_text.sort()
            compressed_text = "".join(compressed_text)

            if not_compressed == compressed_text:
                return compressed_text

            not_compressed = "".join(compressed_text)

    else:
        return "Invalid input !!!"


print(compression(input("Enter your number:   ")))
