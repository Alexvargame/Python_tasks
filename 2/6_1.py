import string
class Alphabet():
    def __init__(self, lang, letters_str):
        self.lang=lang
        self.letters=list(letters_str)
    def print(self):
        str_=(' ').join(self.letters)
        print(str_)
    def letters_num(self):
        print(len(self.letters))

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)
        self.__letters_num=26
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False
    def letters_num(self):
        return self.__letters_num
    @staticmethod
    def example():
        return "This is"
if __name__ == '__main__':
    eng_al=EngAlphabet()
    eng_al.print()
    print(eng_al.letters_num())
    print(eng_al.is_en_letter("F"))
    print(eng_al.is_en_letter("Щ"))
    print(eng_al.example())
                         
