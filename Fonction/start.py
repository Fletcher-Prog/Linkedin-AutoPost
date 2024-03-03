import Fonction as mypackage
from datetime import datetime 
from random import randint
import time



def start(fletchNews :bool):
    
    lancement = 1
    
    while True :
        
        if datetime.now().strftime("%H:%M:%S") == "00:10:00" or lancement ==1   :         

            # Récupération du prompts de création du poste 
            promptDesPosteDuJour = mypackage.recupToutLesPostesDuJour(fletchNews)
            
            if promptDesPosteDuJour == -4 :
                
                lancement = 2                
                break


            # Récupération du poste en fonction du choix fait par mail  
            posteChoisi = mypackage.traitementDesPostes(promptDesPosteDuJour)

            # récupération de la date de publication     
            for idpost , promptValue in promptDesPosteDuJour.items():
                heureDePublication = promptValue["hourStart"] 
                
            # Géneration de l'image pour le poste 
            #if randint(1,2) == 1 :                
            prompImage = "Génere moi une image qui correspond a ce poste " + posteChoisi
            imageUrl = mypackage.recupereImage(prompt=prompImage)  
            success = mypackage.downloadAndSaveImage(imageUrl, "./test.png",fletchNews)
            
            mypackage.posteSurLinkedinAvecImage( posteChoisi,heureDePublication,"./test.png",fletchNews )            

           
            #mypackage.posteSurLinkedin(posteChoisi,heureDePublication,fletchNews)
