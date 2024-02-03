import requests
import Fonction as mypackage
from datetime import datetime 


def posteSurLinkedin(poste,heureDePublication,fletchNews :bool):
    
    while True :
        
        if datetime.now().strftime("%H:%M:%S") == heureDePublication   : 
               
            if fletchNews:
                accessToken = mypackage.accessTokenLinkedinFletchNews
                organizationId = mypackage.organizationIdFletchNews
            else:
                accessToken = mypackage.accessTokenLinkedinFletchOil
                organizationId = mypackage.organizationIdFletchOil 
                
            
            # ID de l'organisation pour FletchOil

            # Préparer les en-têtes de la requête
            headers = {
                'Authorization': f'Bearer {accessToken}',
                'X-Restli-Protocol-Version': '2.0.0',
                'Content-Type': 'application/json'
            }
            # Corps de la requête pour créer le post
            post_data = {
                'author': f'urn:li:organization:{organizationId}',
                'lifecycleState': 'PUBLISHED',
                'specificContent': {
                    'com.linkedin.ugc.ShareContent': {
                        'shareCommentary': {
                            'text': f'{poste}'
                        },
                        'shareMediaCategory': 'NONE'
                    }
                },
                'visibility': {
                    'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'
                }
            }

            # URL de l'API pour créer le post
            url = 'https://api.linkedin.com/v2/ugcPosts'


            # Envoyer la requête POST
            response = requests.post(url, headers=headers, json=post_data)

            # Vérifier la réponse
            if response.status_code == 201:
                print("Post créé avec succès.")
            else:
                print(f"Échec de la création du post: {response.content}")
            
            break