import openai 
import time
import Fonction as mypackage

async def creatPost(prompt):
    
    mypackage.gptClient
    # Ciblage de l'assistant a utilise
    my_assistants = mypackage.gptClient.beta.assistants.retrieve(mypackage.gptIdAssistant)
    print(my_assistants)

    # Création du thread pour la conversation avec l'assistant
    thread = await openai.beta.thread.create()

    await openai.beta.threads.messages.create(thread.id,{role:"user", content: prompt })

    run = await  openai.beta.threads.runs.create(
        thread.id,
        { assistant_id: mypackage.gptIdAssistant }
    )

    runStatus = await openai.beta.threads.runs.retrieve(
            thread.id,
            run.id
          )
    
    while runStatus.status != 'completed' :
            await time.sleep(1)
            runStatus = await openai.beta.threads.runs.retrieve(thread.id, run.id);
    
    messagesResponse = await openai.beta.threads.messages.list(thread.id)

    aiMessages =  [msg for msg in messagesResponse['data'] if msg['role'] == 'assistant']
    
    return aiMessages[aiMessages.length - 1].content[0].text.value;









