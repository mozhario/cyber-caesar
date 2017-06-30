class Alphabet:
    """Cyclic iterable class, that represents alphabet."""
    def __init__(self, start, end, up_start=None, up_end=None, other=None):
        """Alphabet is represented by the bounds of characters ASCII codes,
        not the sequences of characters:
        start - alphabet first character
        end - alphabet last character
        up_start - uppercase alphabet first character (optional)
        up_end - uppercase alphabet last character (optional)
        other - any characters you want! list of attitional characters"""
        self.start = ord(start)
        self.end = ord(end)
        self.up_start = ord(up_start)
        self.up_end = ord(up_end)
        self.other = [ord(char) for char in other]

    def get_all_characters_codes(self):
        return list(range(self.start, self.end)) + \
                list(range(self.up_start, self.up_end)) + \
                self.other

    def get_all_characters(self):
        codes = self.get_all_characters_codes()
        return "".join([chr(code) for code in codes])


if __name__=="__main__":
    alph = Alphabet("a", "z", "A", "Z", [" ", "."])
    print(alph.get_all_characters())