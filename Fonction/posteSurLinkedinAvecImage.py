import Fonction as mypackage
from datetime import datetime 
import requests

def posteSurLinkedinAvecImage(poste,heureDePublication,pathImage,fletchNews :bool):
    
    while True :
        
        if datetime.now().strftime("%H:%M:%S") == heureDePublication   : 
               
            if fletchNews:
                accessToken = mypackage.accessTokenLinkedinFletchNews
                organizationId = mypackage.organizationIdFletchNews
            else:
                accessToken = mypackage.accessTokenLinkedinFletchOil
                organizationId = mypackage.organizationIdFletchOil            
                


        # Préparer les en-têtes de la requête pour l'upload de l'image
        headers_upload = {
            'Authorization': f'Bearer {accessToken}',
            'X-Restli-Protocol-Version': '2.0.0'
        }

        # Préparer la requête pour obtenir l'emplacement d'upload de l'image
        register_upload_data = {
            "registerUploadRequest": {
                "recipes": [
                    "urn:li:digitalmediaRecipe:feedshare-image"
                ],
                "owner": f'urn:li:organization:{organizationId}',
                "serviceRelationships": [
                    {
                        "identifier": "urn:li:userGeneratedContent",
                        "relationshipType": "OWNER"
                    }
                ]
            }
        }

        # URL pour enregistrer l'upload de l'image
        url_register_upload = 'https://api.linkedin.com/v2/assets?action=registerUpload'

        # Faire la requête pour obtenir l'emplacement d'upload
        response_upload = requests.post(url_register_upload, headers=headers_upload, json=register_upload_data)

        if response_upload.status_code == 200:
            upload_url = response_upload.json().get('value').get('uploadMechanism').get('com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest').get('uploadUrl')
            asset = response_upload.json().get('value').get('asset')
            
            # Uploader l'image PNG
            with open(pathImage, 'rb') as image_file:
                image_data = image_file.read()
            headers_image_upload = {
                'Authorization': f'Bearer {accessToken}',
                'Content-Type': 'image/png'  # Spécifier le Content-Type pour une image PNG
            }
            response_image_upload = requests.put(upload_url, headers=headers_image_upload, data=image_data)
            
            # Vérification de la réponse d'upload
            if response_image_upload.status_code in [200, 201]:
                mypackage.logger.info("Image PNG uploadée avec succès.")
                
                # Suivre la suite du processus pour créer le post avec l'image...
            else:
                mypackage.logger.info(f"Échec de l'upload de l'image PNG. Statut: {response_image_upload.status_code}, Réponse: {response_image_upload.text}")
        else:
            mypackage.logger.info(f"Échec de l'enregistrement de l'upload: Statut: {response_upload.status_code}, Réponse: {response_upload.text}")

        headers = {
            'Authorization': f'Bearer {accessToken}',
            'X-Restli-Protocol-Version': '2.0.0',
            'Content-Type': 'application/json'
        }

        # Modification du corps de la requête pour inclure l'image dans le post
        post_data = {
            'author': f'urn:li:organization:{organizationId}',
            'lifecycleState': 'PUBLISHED',
            'specificContent': {
                'com.linkedin.ugc.ShareContent': {
                    'shareCommentary': {
                        'text': poste
                    },
                    'shareMediaCategory': 'IMAGE',
                    'media': [
                        {
                            "status": "READY",
                            "description": {
                                "text": "Description de l'image"
                            },
                            "media": asset,
                            "title": {
                                "text": "Titre de l'image"
                            }
                        }
                    ]
                }
            },
            'visibility': {
                'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'
            }
        }

        # URL de l'API pour créer le post avec l'image
        url = 'https://api.linkedin.com/v2/ugcPosts'

        # Envoyer la requête POST pour créer le post avec l'image
        response = requests.post(url, headers=headers, json=post_data)

        # Vérifier la réponse
        if response.status_code == 201:
            mypackage.logger.info("Post avec image créé avec succès.")
        else:
            mypackage.logger.info(f"Échec de la création du post avec image: {response.status_code}, Réponse: {response.text}")
