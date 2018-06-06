import smtplib, config

def send_email(subject, msg):
    """
    send an email
    :return: True if it goes well, False in other case
    """
    try:
        #connection
        server = smtplib.SMTP('smtp.gmail.com:587')

        #configuration
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_FROMADDRESS, config.PASSWORD)

        #send the mail
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_FROMADDRESS, config.EMAIL_TOADDRESS, message)

        server.quit()

    except:
        return False

    return True
