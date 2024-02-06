
# Acess Notion
from notion_client import Client

# NOTION
NOTION_TOKEN = "secret_V8rwKovb0fizmX8LFqlGmvTMDEhMWPfrJ3EQGL6I9Ct"
notion = Client(auth=NOTION_TOKEN)
databaseIdFletchNews = "ff678a33af78455caf3ff5c8a9211300"
databaseIdFletchOil  = "6ffcb3f144df45f29d3622c8910115be"

# OPENAI
OPENAI_API_KEY = "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"
gptIdAssistant = "asst_UZRLhjwPROjY8MwNtLaO7ypP"

# GMAIL
smtpAddress   = 'smtp.gmail.com'
smtpPort      = 465
emailAdress   = 'aarab.anas04@gmail.com'
emailPassword = 'vbjs vsbt whso zkgp'


#Linkedin 
accessTokenLinkedinFletchOil = 'AQW6EWNHJ6WH27H6Um_rwLRJPLSWcVrJJ8CJCgbAKMn_FTIlAdimA5vm4E6n1YLA-DQYulJ5Stj2oxX0rkaPWbKjR-RVzJ2cq3tjiEZR_OBrFDgCx4KUMGCqBqX21Wh1pHvzbKMhSSYMMur6SXOtbrfQpRQd_Zc7yCD4zRv1JWvIVpE8onoOJsj5Oe253aXoTl8tf2hL_nBHcJZNz9JOjP_WzpAsfm3Pie63DA-4zSx2DpzMNPbKHug-zH5OUUervqAEA1p-Z6S88XexQRXcQ0ADYT8JZy4td95TIRUmoSj1eZOb_fxSqoZ3ign1neFfucDGEscANMBliOUpNnu0_EmZuJOy7g'
organizationIdFletchOil      = 101833561  # ID de l'organisation pour FletchOil

accessTokenLinkedinFletchNews = 'AQUREuDJExkrrsZ0Hx1NnjmbcvsRfQR64iwy45ie0HdnxYuDehDsBe1yk2HuPGhDe-gchZmBssLTigWiJG5JOMrkSB9uZ1Ct-qYaN-UPuU7NJplUs8qH6g-lBXDYZTLWSGehtPCp_WNs_Y5_C_h4znZYNstMpPP60Q9VbaUdfmG5ym-lvytIrljyVlT44uNMBltig3jk6czHAF6IOLZtHd1iy-2lx8tvDj5R0SpNGb-3KXLaf52ZDbbSSfUPZxw_dHOawltpV4rxsT8JJdDfkIEOkky_4uTuOSvYzwqz6eNphz7yB7eLu2Grhj7x0x_pV_UfmuVhHcRPBJD5f61J6yaMzRYD5w'
organizationIdFletchNews      = 101861504  # ID de l'organisation pour FletchNews

# Gestion des logs 
import logging


#Configuration de la forme de base pour l'écriture des log en console
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     datefmt='%Y-%m-%d %H:%M')

# Configuration du loggeur
logger = logging.getLogger("Bot post linkedin")
logger.setLevel(logging.INFO)

# Configuration du ficher ou écrire les log avec le niveau de log a écrire
fileHandler = logging.FileHandler('BotPostLinkedin.log')
fileHandler.setLevel(logging.INFO)

formateur = logging.Formatter("%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M")
fileHandler.setFormatter(formateur)

logger.addHandler(fileHandler)



