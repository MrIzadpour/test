word = input("Please enter your word: ")

new_word = ''
list_1 = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U']
# x = "aAeEoOiIuU"
# y = ".........."

# mytable = word.maketrans(x, y)

for items in word:
    if items == " ":
        continue
    elif items in list_1:
        items = "."
    elif items.islower():
        items = items.upper()
    elif items.isupper():
        items = items.lower()
    new_word = new_word + items

print(new_word)
