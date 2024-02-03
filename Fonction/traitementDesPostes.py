import Fonction as mypackage
import time

def traitementDesPostes(lesPosteDuJour):
    
    for idpost , promptValue in lesPosteDuJour.items():

        promptValue = promptValue['prompt']
            
        print("prompt Envoyer ")
        tabPost = mypackage.createTableauPost(prompt=promptValue)    
        print("post Recu : ")

        # Envoye du mail avec les posts du jours est retourne l'objet du mail 
        objetMail = "Re: {}".format(mypackage.sendEmail(tabPost[0],tabPost[1],tabPost[2]))

        print("Envoye du mail ")

        while True :

            reponse = int(mypackage.receiveEmail(objetMail))

            if reponse == 0:
                
                mypackage.sendEmail("Relance du programme")
            
                return -1 
            

            if reponse > 0 and reponse < 4 :
                              
               return tabPost[reponse -1]
            
            
            time.sleep(15)