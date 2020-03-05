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
# Var
path = r"C:\Users\Bamba\Documents\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)
choice = 0
link = "https://www.boursorama.com/cours/analyses/AAPL/"
element = "c-faceplate__price " 
#

# def
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
		# print("\n--> Apple : ", newPost," USD")

	return newPost
def emailSender():
	
#

# Debut du programme

print("\nHi ! I am Goerge\n")

# Menu

while(choice != 1 and choice != 2 and choice != 3 and choice != 4):
	menu()
	choice = int(input("Choose one of them : "))

# Choix numero 1
if(choice == 1):
	print("\nVous avez choisi :", choice)

	# extraire le text du html pour le stocker dans une variable
	# par la class="c-faceplate__price"
	# tag <div></div>
	
	extracteur(driver, link, element)


	'''
	# va envoyer l'extrait du text pris du text par email
	email_user = 'monamiegoerge@gmail.com'

	email_send = 'monamiegoerge@gmail.com'

	server = smtplib.SMTP('smtp.gmail.com', 587)

	server.starttls()


	server.login(email_user, 'gangawix99')


	message = post.text

	try:
		server.sendmail(email_user, email_send, message)
		print("email sent")
	except:
		print("error")
	server.quit()

	print("Success: send it !")

'''
	driver.quit()