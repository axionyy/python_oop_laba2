class Text:
    def __init__(self, text):
        self.__text = text

    def len_text(self):
        return len(self.__text)

    def letter_count(self):
        count = 0
        for i in self.__text:
            if i.isalpha():
                count += 1
        return count