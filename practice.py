import winsound

# # Play Windows exit sound.
# winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
#
# # Probably play Windows default sound, if any is registered (because
# # "*" probably isn't the registered name of any sound).
# winsound.PlaySound("*", winsound.SND_ALIAS)

# winsound.Beep(600, 1000)
# winsound.MessageBeep()

# Python program to implement Morse Code Translator

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'ا': '.-', 'ب': '-...',
                   'س': '-.-.', 'د': '-..', 'ع': '.',
                   'ف': '..-.', 'ق': '--.', 'ح': '....',
                   'I': '..', 'ج': '.---', 'ک': '-.-',
                   'ل': '.-..', 'م': '--', 'ن': '-.',
                   'و': '---', 'پ': '.--.', 'غ': '--.-',
                   'ر': '.-.', 'ص': '...', 'ت': '-',
                   'ط': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'ی': '-.--', 'ز': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


# Function to decrypt the string
# from morse to english
def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += MORSE_CODE_DICT.keys()[(MORSE_CODE_DICT.values()).index(citext)]
                print(decipher)
                citext = ''

    return decipher


# Hard-coded driver function to run the program
def main():
    message = "مطمعنن میدونستی دوست دارم"
    result = encrypt(message.upper())
    print(result)

    message = "-- ..- -- . -. -.  -- -.-- -.. --- -. -.-. - -.--  -.. --- -.-. -  -.. .- .-. -- "
    result = decrypt(message)
    print(result)


# Executes the main function
if __name__ == '__main__':
    main()
