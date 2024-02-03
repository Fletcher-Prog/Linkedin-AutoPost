import Fonction as mypackage
import time

def createTableauPost(prompt):

    tabPost = []

    for i in range(0,4,1):

        post = mypackage.creatPost(prompt=prompt)

        #print(post)

        #time.sleep(2)

        tabPost.append(post)


    return tabPost



