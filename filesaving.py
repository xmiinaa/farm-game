# imports the library needed for functions in this file
import json

def saveGame(saveID, name, playerX, playerY, cameraX, cameraY, money, location, gender, inventory, tilemap, day, season, hour, minute, weather, dayDuration, elapsedRealTime):
    saveFile = f"{saveID}.json" # creates the name of the save file

    # formats data to store in json file
    information = {
        "name" : name,
        "playerX": playerX,
        "playerY": playerY,
        "cameraX": cameraX,
        "cameraY": cameraY,
        "money": money,
        "location": location,
        "gender": gender,
        "inventory": inventory,
        "tilemap": tilemap,
        "day": day,
        "season": season,
        "hour": hour,
        "minute": minute,
        "weather": weather,
        "dayDuration": dayDuration,
        "elapsedRealTime": elapsedRealTime
    }

    # creates a json object to write to file
    jsonObject = json.dumps(information, indent = 18)

    # opens file in write mode
    with open(saveFile, "w") as outfile:
        outfile.write(jsonObject) # writes the data to the file

# loads the json file and returnsit
def loadGame(saveID):
    saveFile = f"{saveID}.json" # creates the name of the save file

    # opens file in read mode
    with open(saveFile, "r") as openFile:
        jsonObject = json.load(openFile) # creates a json object to store information in
    
    return jsonObject # returns data
