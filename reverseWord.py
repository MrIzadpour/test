Word = str(input("Please Insert your Word:"))

reversedWord = ''

for letter in Word:
    reversedWord = letter + reversedWord

if reversedWord.lower() == Word.lower():
    print("Palindrome")
else:
    print("Not Palindrome")

# # راه حل دوم برای عکس کردن کلمه

# reversed_word = Word[::-1]

# if reversed_word == Word:
#     print("Palindrome")
# else:
#     print("Not Palindrome")