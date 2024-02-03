import threading
import Fonction as mypackage


fletchOil  = threading.Thread(target=mypackage.start,args=(False,))
fletchNews = threading.Thread(target=mypackage.start,args=(True,))

fletchOil.start()
fletchNews.start()





