import smtplib, ssl


def send_mail(message):
    username = "muralimano86@gmail.com"
    password = "yjfqvoqtuvatxizd"

    receiver = "muralimano86@gmail.com"

    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    email_address = "hemalinivaithy@gmail.com"
    message = f"""\
Subject: {email_address}
How are you?
Bye!
"""
    send_mail(message)