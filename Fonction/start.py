import Fonction as mypackage
from datetime import datetime 
import time



def start(fletchNews :bool):
    
    while True :
        
        if datetime.now().strftime("%H:%M:%S") == "00:10:00"   :         

            # Récupération du prompts de création du poste 
            promptDesPosteDuJour = mypackage.recupToutLesPostesDuJour(fletchNews)


            # Récupération du poste en fonction du choix fait par mail  
            posteChoisi = mypackage.traitementDesPostes(promptDesPosteDuJour)

            
            # Géneration de l'image pour le poste 
            #prompImage = "Génere moi une image qui correspond a ce poste " + posteChoisi
            #imageUrl = mypackage.recupereImage(prompt=prompImage)  
            #success = mypackage.downloadAndSaveImage(imageUrl, "./test.png")
            
            # récupération de la date de publication     
            for idpost , promptValue in promptDesPosteDuJour.items():
                heureDePublication = promptValue["hourStart"] 
            
            mypackage.posteSurLinkedin(posteChoisi,heureDePublication,fletchNews)
