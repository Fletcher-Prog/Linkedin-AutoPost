import Fonction as mypackage
import time

def traitementDesPostes(lesPosteDuJour):
    
    for idpost , promptValue in lesPosteDuJour.items():

        promptValue = promptValue['prompt']
            
        mypackage.logger.info("prompt Envoyer ")
        tabPost = mypackage.createTableauPost(prompt=promptValue)    
        mypackage.logger.info("post Recu : ")

        # Envoye du mail avec les posts du jours est retourne l'objet du mail 
        objetMail = "Re: {}".format(mypackage.sendEmail(tabPost[0],tabPost[1],tabPost[2]))

        mypackage.logger.info("Envoye du mail ")

        while True :

            reponse = int(mypackage.receiveEmail(objetMail))

            if reponse == 0:
                
                mypackage.sendEmail("Relance du programme")
            
                return -1 
            

            if reponse > 0 and reponse < 4 :
                              
               return tabPost[reponse -1]
            
            
            time.sleep(15)