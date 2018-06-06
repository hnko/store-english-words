import csv
from Word import *

#delimiter of the meanings in the csv
DELIMITER = '#'

class Application:

    """
    Application class - we store all the words that we are going to introduce on the system
    """
    __singleton = None
    words = list()

    def __init__(self, file_name='notes_english.csv'):
        """
        constructor of the class
        :param file_name: name of the file which we are going to use
        """
        self.file_name = file_name

    #singleton pattern
    def __new__(cls, *args, **kwargs):
        """
        Singleton pattern
        :param args: args
        :param kwargs: kwargs
        :return: __singleton - instance
        """
        if cls.__singleton == None:
            cls.__singleton = object.__new__(Application)
        return cls.__singleton

    def __contains__(self, item):
        print('ENTRA')
        """
        Check if words contains the item
        :param item: Word class
        :return: True if the item is in the words, False in other case
        """
        return True if item in self.words else False

    def add(self, word):
        """
        Append a new word in the application - if the word already exist change the meaning if was passing
        :param word: Word class
        """
        if word not in self.words:
            self.words.append(word)
        elif word.translation != None:
            for w in word.translation:
                self.words[self.words.index(word)].add_meaning(w)

    def drop(self, word):
        """
        Delete a word from the application
        :param word: Word class
        :return: True if the word is remover, False in other case
        """
        try:
            self.words.remove(word)
        except ValueError:
            return False
        return True


    def __str__(self):
        """
        Convert the Class to string
        :return: string with all the data of the Class
        """
        out = '\t\t-------\n\t\t Words \n\t\t-------\n\n'
        for e, i in enumerate(self.words):
            out += str(e+1) + '. ' + str(i) + '\n'
        return out


    def search_word(self, word_to_search):
        """
        search a word by the word in english, return a word class string
        :param word_to_search: Word class
        :return: a string with all the data of the Word or an empty string
        """
        if word_to_search in self.words:
            index_word = self.words.index(word_to_search)
            word = self.words[index_word]

            #increasing the number of searches
            word.searches += 1

            return str(word) + '\n searched {} times.'.format(word.number_of_searches())
        else:
            return ''


    def save(self):
        """
        Save the data into a csv
        """
        with open(self.file_name, 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(['word', 'meaning', 'number_of_searches'])
            for word in self.words:
                csv_writer.writerow([word.get_word(), DELIMITER.join(word.meaning()), word.number_of_searches()])

            print('... data saved ...')

    def load(self):
        """
        Load the data from the csv file
        """
        with open(self.file_name) as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for word in reader:
                self.add(Word(word[0], word[1].split(DELIMITER), word[2]))
            print('... data loaded ...')

    def show_historical(self):
        """
        Show the frequency of searching the data
        :return: a string with the firts 10 datas if there are 10 elements, if not just the elements that it has
        """
        out = ''

        #sort in descending order by the number of sources of the word
        ordered_list = sorted(self.words, key=lambda word: word.searches,reverse=True)

        #take the first 10 elements of the ordered list, if the len of that is less take all of it
        len_ordered_list = 10 if len(ordered_list) > 10 else len(ordered_list)

        for i in range(len_ordered_list):
            out += ordered_list[i].get_word() + ' ' + str(ordered_list[i].searches) + '\n'
        return out
