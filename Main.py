import Fonction as mypackage
from datetime import datetime 

# Récupération de tout les publications programée notion
allPage = mypackage.getDataBaseData()

print(allPage)

# Traitement afin de récupére que les donnée qui nous intéresse
toutLesPostesProgramme = {}
for page in allPage:
    page_id = page['id']
    prompt_string = mypackage.extractStringFromPrompt(page)
    status_name = mypackage.extractStatusName(page)
    start_date = mypackage.extractStartDate(page)
    toutLesPostesProgramme[page_id] = {
        'prompt': prompt_string,
        'statusName': status_name,
        'startDate': start_date,
        'heureDePublication' :start_date ,
    }


toutLesPosteDuJour = {}

dateDuJour = datetime.now().strftime("%Y-%m-%d")

# Parcours de chaque element du tableau de donnée souhaité
for page_id, data in toutLesPostesProgramme.items():
    print(f"Page ID: {page_id}, Prompt String: {data['prompt']}, Status Name: {data['statusName']}, Start Date: {data['startDate']}","\n")

    if data['startDate'] == dateDuJour :
        
        toutLesPosteDuJour[page_id] = data

    print(toutLesPosteDuJour)


