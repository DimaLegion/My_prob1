import string


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        return self.letters

    def letters_num(self):
        print(len(self.print()))


class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_lowercase)

    def __init__(self):
        super().__init__(lang='En', letters=string.ascii_lowercase)

    def is_en_letter(self, let):
        Alfa = ''
        for item in self.letters:
            if item == let:
                Alfa = item
                print(f'буква {Alfa} принадлежит этому алфавиту {self.lang}')
        if let not in self.letters:
            print(f'буква {let} непринадлежит этому алфавиту {self.lang}')

    def letters_num(self):
        print(f'Количество букв в алфавите', self.__letters_num)

    @staticmethod
    def example():
        print('hello world, happy!')


if __name__ == '__main__':
    a1 = EngAlphabet()
    print(a1.print())
    a1.letters_num()
    a1.is_en_letter('f')
    a1.is_en_letter('щ')
    a1.example()
