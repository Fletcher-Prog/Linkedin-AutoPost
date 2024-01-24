import openai 
import time
import json
import Fonction as mypackage




def creatPost(prompt):
    
    client = openai.OpenAI(api_key=mypackage.OPENAI_API_KEY)

    # Ciblage de l'assistant a utilise
    my_assistants = client.beta.assistants.retrieve(mypackage.gptIdAssistant)
    #print(my_assistants)
    
    # Création du thread pour la conversation avec l'assistant
    thread = client.beta.threads.create()

    # Création du message
    client.beta.threads.messages.create(thread.id,role="user", content=prompt )

    # Initialisation du thread de discution avec le bonne étudiant
    run = client.beta.threads.runs.create(
        thread.id,
        assistant_id= mypackage.gptIdAssistant
    )

    # Envoi du message
    runStatus = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    
    # Attendre que l'ai réponde
    while runStatus.status != 'completed' :
            time.sleep(1)
            runStatus = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    
    messagesResponse = client.beta.threads.messages.list(thread.id)

    # "Convestion de la réponde en JSON
    messagesResponseJson = json.loads(messagesResponse.model_dump_json())

    return  messagesResponseJson['data'][0]['content'][0]['text']['value']









