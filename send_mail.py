import smtplib, ssl


def send_mail(email_address, message):
    username = "muralimano86@gmail.com"
    password = "yjfqvoqtuvatxizd"

    receiver = "muralimano86@gmail.com"

    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    message = f"""\
Subject: {email_address}
{message}
"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    email_address = "hemalinivaithy@gmail.com"
    message = """
    How are you?
    Bye!
    """
    send_mail(email_address, message)