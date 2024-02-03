from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
from datetime import datetime 
import Fonction as mypackage


def sendEmail(post1,post2="",post3=""):

  # on rentre les renseignements pris sur le site du fournisseur
  smtpAddress = mypackage.smtpAddress
  smtpPort = mypackage.smtpPort
  # on rentre les informations sur notre adresse e-mail
  emailAdress = mypackage.emailAdress
  emailPassword = mypackage.emailPassword

  date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  # on rentre les informations sur le destinataire
  emailReceiver = 'aarabanas10pro@gmail.com'

  # on crée un e-mail
  message = MIMEMultipart("alternative")
  # on ajoute un sujet
  message["Subject"] = "Poste Réseaux du jour : {} " .format(date)
  # un émetteur
  message["From"] = ""
  # un destinataire
  message["To"] = "aarabanas10pro@gmail.com"

  # on crée un texte et sa version HTML
  texte = ''' Poste 1 : \n {} \n\n  Poste 2 : \n {} \n\n Poste 3 : \n {} \n\n\n\n INFO : \n 0 : Relance programme \n 4 : Relance programme demain \n Post 1 : 1 \n Post 2 : 2 \n Post 3 : 3 '''.format(post1,post2,post3)


  # on crée deux éléments MIMEText 
  texte_mime = MIMEText(texte, 'plain')

  # on attache ces deux éléments 
  message.attach(texte_mime)

  # on crée la connexion
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtpAddress, smtpPort, context=context) as server:
    
    # connexion au compte
    server.login(emailAdress, emailPassword)
    
    # envoi du mail
    server.sendmail(emailAdress, emailReceiver, message.as_string())

    return message["Subject"]
