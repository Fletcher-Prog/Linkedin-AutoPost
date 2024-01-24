import Fonction as mypackage
from datetime import datetime 
import asyncio

# Récupération de tout les publications programée notion
allPage = mypackage.getDataBaseData()

# Traitement afin de récupére que les donnée qui nous intéresse
toutLesPostesProgramme = {}

for page in allPage:

    page_id = page['id']    

    prompt_string = mypackage.extractStringFromPrompt(page)
    status_name   = mypackage.extractStatusName(page)
    start_date    = mypackage.extractStartDate(page)
    
    toutLesPostesProgramme[page_id] = {
        "prompt": prompt_string,
        "statusName": status_name,
        "startDate": start_date,
        "hourStart" : ""        
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


#print(toutLesPosteDuJour)

prompt_value = toutLesPosteDuJour['7f4fb6e4-2c31-4147-9201-36e474bc90a2']['prompt']

print("prompt Envoyer ")

post = mypackage.creatPost(prompt=prompt_value)
extracted_texts = []


print("post Recu")

print("---------------------------------------------------------------------------------------------------------------")

print(post)

print("---------------------------------------------------------------------------------------------------------------")



for message in post:

    if message == "content=" :
        print(message)


#print(post)
