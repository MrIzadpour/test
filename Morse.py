import winsound
from abc import ABC, abstractmethod
from os import name, system


class Morse(ABC):
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', '\n': '|', ' ': '/',
        ', ': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'
    }
    Morse_Code_Dict_reverse = {value: key for key, value in MORSE_CODE_DICT.items()}

    def print(self):
        return self.Morse_Code_Dict_reverse

    def __init__(self, data: str) -> None:
        self._data = data
        assert self._check()

    @abstractmethod
    def process(self) -> str:
        """
        Tabdil mikne data ro be codinge morede nazar!
        """
        pass

    @abstractmethod
    def _check(self) -> bool:
        """
        Check mikne ke data qabele estefade baraie ma hast!!!
        :param data:
        """
        pass

    def save_file(self, file_name):
        with open(file_name, 'w') as f:
            f.write(self.process())

    @classmethod
    def from_file(cls, file_path):
        """
        Sakhtane yek nemoone ba estefade az file!
        :param file_path:
        :return:
        """
        with open(file_path) as f:
            data = f.read()
            return cls(data)  # MorseEncoder / MorseDecoder

    def str(self):
        return self.process()

    @staticmethod
    def to_beep(data):
        if isinstance(data, MorseEncoder):
            if name == "posix":
                res = data.process()
                for res_item in res:
                    if res_item == '.':
                        system('( speaker-test -t sine -f 1000 ) & pid=$! ; sleep 0.1s ; kill -9 $pid')
                    elif res_item == '-':
                        system('( speaker-test -t sine -f 900 ) & pid=$! ; sleep 0.1s ; kill -9 $pid')
                    elif res_item == '/':
                        system('( speaker-test -t sine -f 500 ) & pid=$! ; sleep 0.1s ; kill -9 $pid')
                    elif res_item == '|':
                        system('( speaker-test -t sine -f 700 ) & pid=$! ; sleep 0.1s ; kill -9 $pid')


class MorseEncoder(Morse):

    def __init__(self, data: str) -> None:
        super().__init__(data)

    def process(self) -> str:
        res = ""
        for c in self._data.replace('  ', ' '):
            res += self.MORSE_CODE_DICT[c.upper()] + ' '
        return res

    def _check(self):
        return all(
            map(
                lambda s: s.isalnum() and s.isascii(),
                self._data.split()
            )
        )


class MorseDecoder(Morse):

    def __init__(self, data: str) -> None:
        super().__init__(data)

    def process(self) -> str:
        res = ""
        for c in self._data.split():
            res += (self.Morse_Code_Dict_reverse[c])
        return res.title()

    def _check(self):
        check_list = ['.', '-', '/', '|']
        return all(
            map(
                lambda s: s in Morse.Morse_Code_Dict_reverse.keys(),
                self._data.split()
            )
        )


e = MorseEncoder("mohammadreza")
# print(e.process())
# Morse.to_beep(e)
# b = MorseDecoder("... .- .-.. .- -- / .- -.- -... .- .-. | .-. . --.. .- ")
bb = MorseDecoder("-- --- .... .- -- -- .- -.. .-. . --.. .-")
print(e.process())
# test2 = b.process()
# print(test2)
# print(Morse.Morse_Code_Dict_reverse)
