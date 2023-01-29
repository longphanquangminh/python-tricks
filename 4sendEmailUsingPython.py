import smtplib
from dotenv import dotenv_values

config = dotenv_values(".env")

my_email = "demoappvilike2@gmail.com"
my_password = config['GMAIL_PASSWORD']

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = my_email, password = my_password)

connection.sendemail(from_addr = my_email, to_addrs = "phanquangminhlongstorage@gmail.com", msg = "Hello World")

connection.close()
