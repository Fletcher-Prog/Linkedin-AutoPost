
import Fonction as mypackage
from datetime import datetime, timedelta
import time

def recupToutLesPostesDuJour(fletchNews :bool) :

    while True : 
        
            # Récupération de tout les publications programée notion
            allPage = mypackage.getDataBaseData(fletchNews=fletchNews)

            # Traitement afin de récupére que les donnée qui nous intéresse
            toutLesPostesProgramme = {}

            for page in allPage:
                page_id = page['id']    

                prompt_string = mypackage.extractStringFromPrompt(page)
                status_name   = mypackage.extractStatusName(page)
                start_date    = mypackage.extractStartDate(page)
                
                toutLesPostesProgramme[page_id] = {
                    "prompt"    : prompt_string,
                    "statusName": status_name,
                    "startDate" : start_date,
                    "hourStart" : "07:55:00"        
                }


            toutLesPosteDuJour = {}

            dateDuJour = datetime.now().strftime("%Y-%m-%d")

            # Parcours de chaque element du tableau de donnée souhaité
            for page_id, data in toutLesPostesProgramme.items():            
                # Formatage de l'heure et de la date comme je le souhaite
                data["hourStart"] = data['startDate'].split("T")[1].split("+")[0].split(".")[0]

                data["startDate"] = data['startDate'].split("T")[0]

                if data["startDate"] == dateDuJour :                   
                    toutLesPosteDuJour[page_id] = data
            
            # cas ou les nombre de post pour ajourd'hui est supérieure a 1
            if len(toutLesPosteDuJour) >= 2:                   
                # Permet de récupére le l'objet du mail afin de faire le teste par la suite
                objetMail =  mypackage.sendEmail("Trop de poste son présent pour ajourd'hui merci de le réctifier")


                while True :
                    
                    reponse = mypackage.receiveEmail("Re: {}".format(objetMail))

                    if reponse == "0":
                        mypackage.sendEmail("Relance du programme")
                        break

                    time.sleep(15)
            else :            

                #Cas ou il n'y a pas de poste dans la base
                if len(toutLesPosteDuJour) == 0:

                    objetMail = mypackage.sendEmail("Aucun poste est présent pour ajourd'hui merci de le réctifier si néssésaire")

                    
                    while True :
                        
                        reponse   = mypackage.receiveEmail("Re: {}".format(objetMail))
                        
                        if reponse == "0": 
                            mypackage.sendEmail("Relance du programme")
                            break

                        if reponse == "4" :                          
                            mypackage.sendEmail("Relance du programme demain")
                            return -4
                        
                        time.sleep(120)

                else :
                    break        
        
    return toutLesPosteDuJour