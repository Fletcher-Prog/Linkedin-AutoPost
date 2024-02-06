import openai 
import Fonction as mypackage

def recupereImage(prompt:str):

  client =  openai.OpenAI(api_key=mypackage.OPENAI_API_KEY)

  response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
  )

  mypackage.logger.info("Image Génere")
  return response.data[0].url