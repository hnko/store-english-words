class Word:
    """
    Word class - useful for store the word and the meaning
    """

    def __init__(self, word, translation=[], searches=0):
        """
        Constructor of the class
        :param word: the word in english
        :param translation: the translation of the english word - by default None
        :param searches: the number of searches that the user did - by default 0
        """
        self.searches = int(searches)
        self.word = word
        self.translation = []
        for i in translation:
            self.translation.append(i)

    def meaning(self):
        """
        Return the translation of the word
        :return: translation of the english word
        """
        return self.translation


    def number_of_searches(self):
        """
        return the number of times that the word was searched
        :return: searches of the word
        """
        return self.searches


    def get_word(self):
        """
        Getter of word
        :return: the word
        """
        return self.word

    def add_meaning(self, meaning):
        """
        Setter of translation
        :param meaning: one meaning
        """
        if meaning not in self.translation:
            self.translation.append(meaning)

    def __eq__(self, other):
        """
        Compare if is equals to the other object
        :param other: Word class
        :return: True if both classes have the same word - in this case doesnt matter the translation, False in other case
        """
        if isinstance(self, other.__class__):
            return self.word == other.word
        return False

    def __str__(self):
        """
        Convert a Word class to a string
        :return: a string with the word and the meaning of a Word class
        """
        out = self.word + ' means: '
        for meaning in self.translation:
            out += meaning + ' / '

        #use the slide because it is not necessary the last '/'
        return out[:-2]
