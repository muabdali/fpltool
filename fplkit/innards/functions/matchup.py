import requests
import json
from associate import Associate

asso = Associate()


class matchupFunctions:
    def __init__(self):
        self.playerList = asso.IDAssociate()
    
    def test(self):
        print(self.playerList)



done = matchupFunctions()
done.test()