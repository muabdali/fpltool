import requests
import json
from associate import Associate

asso = Associate()


class matchupFunctions:
    def __init__(self):
        self.playerList = asso.IDAssociate()
        self.chosenID = 0
        self.currentMW = asso.currentMWValue()
        self.teamInfoLink = f"https://draft.premierleague.com/api/entry/{self.chosenID}/public"
    def currentPoints(self, playerID):
        self.chosenID = playerID
        response = requests.get(self.teamInfoLink)
        data = json.loads(response.text)
        print(data)



        

a = matchupFunctions()
a.currentPoints()

