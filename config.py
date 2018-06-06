FILE = 'personal_data.txt'

# open the file to read the email_from, password and email_to
with open(FILE, 'r') as f:
    #the way to store the data is just a line delimiter by ','
    EMAIL_FROMADDRESS, PASSWORD, EMAIL_TOADDRESS = f.read().split(',')

def change_address_to(toaddress):
    """
    change the default address to send the email
    :param toaddress: new address
    """
    global EMAIL_TOADDRESS
    EMAIL_TOADDRESS = toaddress

    with open(FILE, 'w') as f:
        f.write(EMAIL_FROMADDRESS + ',' + PASSWORD + ',' + EMAIL_TOADDRESS)

def change_address_from(fromaddress, password):
    """
    change the address from where we send the email
    :param fromaddress: new fromaddress
    :param password: the password of the new address
    """
    global EMAIL_FROMADDRESS, PASSWORD
    EMAIL_FROMADDRESS = fromaddress
    PASSWORD = password

    with open(FILE, 'w') as f:
        f.write(EMAIL_FROMADDRESS + ',' + PASSWORD + ',' + EMAIL_TOADDRESS)
