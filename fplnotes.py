"""
Here are the API endpoints for the draft game

https://draft.premierleague.com/api/bootstrap-dynamic

https://draft.premierleague.com/api/game # kinda useless

https://draft.premierleague.com/api/bootstrap-static

https://draft.premierleague.com/api/league/{League_ID}/details

https://draft.premierleague.com/api/league/{League_ID}/element-status

https://draft.premierleague.com/api/draft/league/{League_ID}/trades

https://draft.premierleague.com/api/draft/entry/{Team_ID}/transactions

https://draft.premierleague.com/api/pl/event-status

https://draft.premierleague.com/api/event/{GW}/live

https://draft.premierleague.com/api/entry/{Team_ID}/public

https://draft.premierleague.com/api/entry/{Team_ID}/my-team

https://draft.premierleague.com/api/draft/{League_ID}/choices

https://draft.premierleague.com/api/watchlist/{Team_ID}

https://draft.premierleague.com/api/entry/{Team_ID}/event/{GW}'










https://draft.premierleague.com/api/bootstrap-dynamic

Contains information of draft league, each team's bootstrap dynamic can only be
viewed by the OWNER of that team, i.e information will be provided about the team
that is logged into that browser.





----------------------------------------------------------


Given any player ID (element), you can subtract 1 and extract information from here:

https://draft.premierleague.com/api/bootstrap-static

under elements.

- JSON data containing information of every football player in premier league, listed as "Elements" (three digit number).
- Gives information such as Goals Scored, asssits, ICT(influence) index, minutes, own goals, cards, starts, xG xA, xGA, Transfer news, injury status and news, creativity, threat rankings, current form, penalty order etc, team ETC.

# Team ID corresponds to team in alphabetical order (example, team ID of 1 is Arsenal)
"""