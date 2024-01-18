import Fonction as mypackage

# Define the async function to search in the database
def searchIdPage(searchPage:str ):
    response = mypackage.notion.search(
        query=searchPage,
        filter={
            "value": "database",
            "property": "object"
        },
        sort={
            "direction": "ascending",
            "timestamp": "last_edited_time"
        }
    )
    return response["request_id"]
