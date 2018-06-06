import Application as a
from Word import *
import sys, os, time
from sendmessage import send_email
from config import change_address_to, change_address_from

#name of the mail subject - in the function it adds the file name
SUBJECT = 'english_notebook'


file_name = input('Introduce the name of the file:\n>>> ')

#Check if the file_name has the termination .csv
if file_name[-4:] != '.csv':
    file_name += '.csv'

app = a.Application(file_name)

#try to load the data if the file already exist
try:
    app.load()
except FileNotFoundError:
    print('You dont have data. Lets start to fill it! :D')


def main_screen():
    """
    main screen - Show all the options
    """
    screen = "(1) Add\n" \
             "(2) Delete\n" \
             "(3) Search\n" \
             "(4) Show words\n" \
             "(5) Show Historical\n"\
             "(6) Send by email\n"\
             "(7) Exit"

    print(screen)
    user_option = input('>>> ')
    while(user_option not in ['1', '2', '3', '4', '5', '6', '7']):
        user_option = input('>>> ')

    if user_option == '1':
        add_screen()
    elif user_option == '2':
        drop_screen()
    elif user_option == '3':
        search_screen()
    elif user_option == '4':
        show_screen()
    elif user_option == '5':
        show_historical()
    elif user_option == '6':
        show_send_email()
    else:
        exit_screen()


def add_screen():
    """
    add screen
    """
    word_to_add = input('(word, meaning)\n>>> ').split(', ')
    len_word = len(word_to_add)

    # the user introduced just the word, not the meaning/s
    if len_word == 1:
        app.add(Word(word_to_add[0]))
    else:
        #word with meaning/s
        app.add(Word(word_to_add[0], word_to_add[1:]))
    os.system('clear')
    main_screen()


def drop_screen():
    """
    drop screen
    """
    word_to_drop = input('>>> ')
    if(not(app.drop(Word(word_to_drop)))):
        print(word_to_drop + ' is not in the system.')
        time.sleep(2)
    else:
        print(word_to_drop + ' deleted from the system.')
        time.sleep(1)
    os.system('clear')
    main_screen()


def search_screen():
    """
    search screen
    """
    word_to_search = input('>>> ')
    word_finded = app.search_word(Word(word_to_search))
    len_search = len(word_finded)

    if len_search == 0:
        print(word_to_search + ' is not in the system.')
        time.sleep(2)
    else:
        print(word_finded)
        input('... press Enter to continue ... ')
    os.system('clear')
    main_screen()

def show_screen():
    """
    show screen - shows all the words that the system has
    """
    print(str(app))
    input('... press Enter to continue ... ')
    os.system('clear')
    main_screen()

def show_historical():
    """
    show the historical of words
    """
    print(app.show_historical())
    input('... press Enter to continue ... ')
    os.system('clear')
    main_screen()

def show_send_email():
    """
    show the send email options and send the email
    """
    os.system('clear')
    screen = "(1) Send\n" \
             "(2) Config To\n" \
             "(3) Config From\n" \
             "(4) Quit"
    print(screen)
    user_option = input('>>> ')

    while(user_option not in ['1', '2', '3', '4']):
        user_option = input('>>> ')

    if user_option == '1':

        status = send_email(SUBJECT + ' '+ file_name, app)
        if status == True:
            print('... email sent ...')
            time.sleep(2)
        else:
            print('... unnable to send the email ...')
            input('... press Enter to continue ... ')
        os.system('clear')
        main_screen()
    elif user_option == '2':
        to = input('>>> ')
        change_address_to(to)
        os.system('clear')
        show_send_email()
    elif user_option == '3':
        from_ = input('>>> ')
        change_address_from(from_)
        os.system('clear')
        show_send_email()
    else:
        os.system('clear')
        main_screen()


def exit_screen():
    """
    exit screen
    """
    app.save()
    sys.exit()
