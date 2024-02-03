import requests

def downloadAndSaveImage(image_url, file_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print("Image télecharger et enregistre")
        return True
    else:
        print("Error lors du télecharger ou enregistrement de l'image")
        return False