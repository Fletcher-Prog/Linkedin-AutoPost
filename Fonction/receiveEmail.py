import imaplib
import email
import Fonction as mypackage
from random import randint

def receiveEmail(object: str):
    # Paramètres de connexion
    host = mypackage.smtpAddress
    username = mypackage.emailAdress
    password = mypackage.emailPassword

    # Connexion au serveur IMAP et sélection de la boîte de réception
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")

    # Préparation de la requête de recherche
    mail.literal  = u'"{}"'.format(object).encode('utf-8')
    typ, data = mail.uid('SEARCH', 'CHARSET', 'UTF-8', 'SUBJECT')

    # Vérifier si des emails ont été trouvés
    if data[0]:
        
        data[0] = data[0].split()

        numDerrnierPost = len(data[0])-1 
        num = data[0][numDerrnierPost]
           
        typ, email_data = mail.uid('fetch', num, '(RFC822)')
        raw_email = email_data[0][1]
        email_message = email.message_from_bytes(raw_email)

        # Traitement de l'email
        # Afficher le sujet et l'expéditeur, par exemple
        # print('From:', email_message['From'])
        # print('Subject:', email_message['Subject'])

        # Récupération du contenu de l'email
        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":  
                    body = part.get_payload(decode=True)
                    #print("Body:", body.decode().split()[0])
        else:
            body = email_message.get_payload(decode=True)
            #print("Body:", body.decode())
    else:
        
        if randint(1,7) == 1 :
            mypackage.logger.info("Aucun email trouvé avec ce sujet.")

    # Déconnexion
    mail.logout()

    try:
        return body.decode().split()[0]
    except:
        return "-1"
