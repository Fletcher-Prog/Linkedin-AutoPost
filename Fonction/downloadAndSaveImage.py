import requests
import Fonction as mypackage

def downloadAndSaveImage(imageUrl, filePath):
    response = requests.get(imageUrl)
    if response.status_code == 200:
        with open(filePath, 'wb') as file:
            file.write(response.content)

        mypackage.logger.info("Image télecharger et enregistre")
        return True
    else:
        mypackage.logger.info("Error lors du télecharger ou enregistrement de l'image")
        return False