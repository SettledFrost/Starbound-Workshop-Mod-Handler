import requests

def fetchWorkshopName(ModID):
    #Steam's Workshop API url
    API_URL = "https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/"

    #Request payload
    data = {
        "itemcount": 1,
        "publishedfileids[0]": ModID
    }

    #Place in the request
    response = requests.post(API_URL, data=data)
    #Check if the request was a success
    response.raise_for_status()

    #Filter mod information
    details = response.json()["response"]["publishedfiledetails"][0]

    #Return the mod's name
    return details["title"]