import smtplib
my_email = "demoappvilike2@gmail.com"
password = ENV['GMAIL_PASSWORD']

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = my_email, password = password)

connection.sendemail(from_addr = my_email, to_addrs = "phanquangminhlongstorage@gmail.com", msg = "Hello World")

connection.close()
