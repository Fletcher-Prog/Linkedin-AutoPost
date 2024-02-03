import Fonction as mypackage

def getDataBaseData(fletchNews :bool):
    

    print("Récupération des ou du promps")
    
    allPage = []
    try:
        
        if fletchNews :            
            results = mypackage.notion.databases.query(database_id=mypackage.databaseIdFletchNews)
            
        else:
            results = mypackage.notion.databases.query(database_id=mypackage.databaseIdFletchOil)

            
            
            
        for page in results.get("results", []):
            
            allPage.append(page)
            
        return allPage  # This will print the raw data of each page (row) in the database
    except Exception as e:
        print(f"An error occurred: {e}")