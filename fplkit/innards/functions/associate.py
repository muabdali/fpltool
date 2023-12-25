# main file, contains the information of all members in league
import requests
import json

"""
league_entries
- gives ID of each user and other informtaion such as full name and join time.

standings
- gives standings in order from top to bottom, also information such as match wins, losses etc, total points etc.



"""

class associate:
    def __init__(self):
        self.playerIDList = {}
        self.League_ID = "69274"
        self.leagueLink = f'https://draft.premierleague.com/api/league/{self.League_ID}/details'
        response = requests.get(self.leagueLink)
        self.data = json.loads(response.text)
        self.entryDict = {}
        


    def IDAssociate(self):
        if 'league_entries' in self.data:
            entries = self.data['league_entries']
            for entry in entries:
                entry_id = entry.get('entry_id')
                entry_name = entry.get('player_first_name')
                player_id = entry.get('id')
                self.playerIDList[entry_name] = player_id
                self.entryDict[player_id] = entry_name
                #print(f"Entry ID: {entry_id}, Entry Name: {entry_name}, Player ID: {player_id}")

            betterplayerIDList = ""
            for entry, player_id in self.playerIDList.items():
                betterplayerIDList = betterplayerIDList + f"{entry} | {player_id} \n"
        else:
            print("No 'league_entries' found in the data.")
        
        return betterplayerIDList
    def standings(self):
        self.IDAssociate()


        stringStandings = "P| NAME |  W  |  L  |  PTS   \n"
        if "standings" in self.data:
            standings = self.data['standings']
            for entry in standings:
                player_name = self.entryDict.get(entry['league_entry'])  # Retrieve player name or "None" if not found
                player_name = str(player_name)
                formatted_name = player_name.ljust(15)  # Adjust the width as needed
                stringStandings += f"{entry['last_rank']} | {formatted_name} | {entry['matches_won']}   |  {entry['matches_lost']}  |  {entry['total']}\n"
        return stringStandings
                
                
        
asso = associate()

asso.standings()