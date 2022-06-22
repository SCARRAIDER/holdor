import smtplib

#Ports 465 and 587 are intended for email client to email server communication - sending email
server = smtplib.SMTP('smtp.gmail.com', 587)

#starttls() is a way to take an existing insecure connection and upgrade it to a secure connection using SSL/TLS.
server.starttls()

#Next, log in to the server
server.login("", "")

msg = "Hello! This Message was sent by the help of Python"

#Send the mail
server.sendmail("", "", msg)