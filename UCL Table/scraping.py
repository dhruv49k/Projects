import requests
from bs4 import BeautifulSoup
import pandas as pd

standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
data = requests.get(standings_url)

soup = BeautifulSoup(data.text)

standings_table = soup.select('table.stats_table')[0]
links = standings_table.find_all('a')
links = [l.get("href") for l in links]
links = [l for l in links if '/squads/' in l]
team_urls = [f"https://fbref.com{l}" for l in links]
inputTeam = input('Enter team name : ')
teamURL = ''
count=0
for i in range(len(team_urls)):
        if inputTeam.lower() in team_urls[i].lower():
            teamURL=team_urls[i]
        else:
            count+=1
if count == len(team_urls) :          
    print("Inputed team not in UEFA Champuons League")
else:
    data = requests.get(teamURL)
    matches = pd.read_html(data.text, match="Scores & Fixtures")[0]
    UCLmatches = matches[matches["Comp"]=="Champions Lg"]
    UCLmatches = UCLmatches[['Date','Time','Day','Venue','Opponent','GF','GA','Result','Captain']]
    UCLmatches['Opponent'] = UCLmatches['Opponent'].str[3:]
  # print(teamName.upper())
    print(UCLmatches)
