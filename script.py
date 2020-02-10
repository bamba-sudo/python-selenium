###########################
## Project by bamba-sudo ##
###########################

# little project on notification selenium

from selenium import webdriver

import smtplib

'''
email_user = 'monamiegoerge@gmail.com'
email_send = 'monamiegoerge@gmail.com'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(email_user, 'gangawix99')

message = 'Hi my friend'

server.sendmail(email_user, email_send, message)

server.quit()

'''

path = r"C:\Users\Bamba\Downloads\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(path)

x = 2
i = 0

while (i<x):
	driver.get('https://www.boursorama.com/cours/analyses/AAPL/')

	posts = driver.find_elements_by_class_name("c-faceplate__price ")

	for post in posts:
		print(post.text)

	i = i + 1

email_user = 'monamiegoerge@gmail.com'
email_send = 'monamiegoerge@gmail.com'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(email_user, 'gangawix99')

message = post.text

server.sendmail(email_user, email_send, message)

server.quit()

print("Success: send it !")

driver.quit()