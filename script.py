###########################
## Project by bamba-sudo ##
###########################

# little project on notification selenium

from selenium import webdriver

import smtplib

from config import *

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

# Var
path = r"C:\Users\Bamba\Documents\chromedriver_win32\chromedriver.exe"
appleLink = "https://www.boursorama.com/cours/analyses/AAPL/"
element = "c-faceplate__price " 
alibabaLink = "https://www.boursorama.com/cours/BABA/"
choix = 1
appleHtml = 'emailV2.html'
#


# ============= def ======================
def menu():
	print("\n1. Apple"
		"\n2. Alibaba"
		"\n3. Facebook"
		"\n4. Choose my stock...")

def extracteur(unDriver, unLink, unElement):
	unDriver.get(unLink)

	posts = unDriver.find_elements_by_class_name(unElement)

	for post in posts:
		newPost = post.text[0:6]

	unDriver.quit()
	return newPost

def emailSender(unPost, unEmailUser, unEmailSender, unHtml):
	server = smtplib.SMTP('smtp.gmail.com', 587)

	server.starttls()

	server.login(unEmailUser, 'gangawix99')

	the_msg = MIMEMultipart("alternative")

	plain_txt = "Testing the message"

	html = open(unHtml).read() %(unPost)

	part_1 = MIMEText(plain_txt, 'plain')
	part_2 = MIMEText(html,"html")

	the_msg.attach(part_1)
	the_msg.attach(part_2)

	print(the_msg.as_string())

	try:
		server.sendmail(unEmailUser, unEmailSender, the_msg.as_string())
		print("Email sent")
	except:
		print("Error")
	server.quit()

		
# ====================================== 

# Debut du programme

print("\nHi ! I am Goerge\n")

while(choix == 1):
	# Menu
	driver = webdriver.Chrome(path)
	choice = 0
	while(choice != 1 and choice != 2 and choice != 3 and choice != 4):
		menu()
		choice = int(input("Choose one of them : "))
	# Choix numero 1
	if(choice == 1):
		print("\nVous avez choisi : Apple")

		# extraire le text du html pour le stocker dans une variable
		# par la class="c-faceplate__price"
		# tag <div></div>
		
		post = extracteur(driver, appleLink, element)

		# va envoyer l'extrait du text pris du text par email
		emailSender(post, EMAIL_USER, EMAIL_SENDER, appleHtml)

	# Choix numero 2
	if(choice == 2):
		print("\nVous avez choisi : Alibaba")

		post = extracteur(driver, alibabaLink, element)

		emailSender(post, EMAIL_USER, EMAIL_SENDER, "Alibaba --> ")

	if(choice == 3):
		print("\nVous avez choisi: Facebook")

		post = extracteur(driver, alibabaLink, element)

		emailSender(post, EMAIL_USER, EMAIL_SENDER, "Facebook --> ")
	if(choice == 4):
		print("\nVous avez choisi: A votre choix")

		indexLink = str(input("\nEntrez votre link ici de boursorama : "))

		nameOfStock = input("\nEntrez le nom du stock ici : ")+" --> "

		post = extracteur(driver, indexLink, element)

		emailSender(post, EMAIL_USER, EMAIL_SENDER, nameOfStock)
	choix = int(input("\nVoulez vous conitnuez - \n1.Oui\n2.Non\n ... "))