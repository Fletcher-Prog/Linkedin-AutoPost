import threading
import Fonction as mypackage


mypackage.logger.info("Start")
fletchOil  = threading.Thread(target=mypackage.start,args=(False,))
fletchNews = threading.Thread(target=mypackage.start,args=(True,))

fletchOil.start()
fletchNews.start()