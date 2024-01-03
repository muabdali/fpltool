import requests
import json
from tabulate import tabulate

class Associate:
    def __init__(self):
        self.playerIDList = {}
        self.entryDict = {}
        self.League_ID = "69274"
        self.leagueLink = f'https://draft.premierleague.com/api/league/{self.League_ID}/details'
        self.fetch_data()
        self.currentMWValue = 0
        self.draftinfo = "https://draft.premierleague.com/api/game"

    def fetch_data(self):
        response = requests.get(self.leagueLink)
        self.data = json.loads(response.text)
        return self.data

    def IDAssociate(self):
        if 'league_entries' in self.data:
            entries = self.data['league_entries']
            for entry in entries:
                entry_id = entry.get('entry_id')
                entry_name = entry.get('player_first_name')
                player_id = entry.get('id')
                self.playerIDList[entry_name] = entry_id
                self.entryDict[entry_id] = entry_name


        else:
            print("No 'league_entries' found in the data.")
        
        return self.playerIDList
    def standings(self):
        self.IDAssociate()

        table_data = []
        if "standings" in self.data:
            standings = self.data['standings']
            for entry in standings:
                player_id = entry.get('league_entry')
                player_name = self.entryDict.get(player_id) or "average"  
                table_data.append([entry['last_rank'], player_name, entry['matches_won'], entry['matches_lost'], entry['total']])

        headers = ["P", "NAME", "W", "L", "PTS"] 
        table = tabulate(table_data, headers=headers, tablefmt='orgtbl')
        return table

    





asso = Associate()
# Fetch data first
asso.fetch_data()
# Get standings table
