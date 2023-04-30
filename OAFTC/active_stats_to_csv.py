"""
Script collects data from the Orange Alliance API and writes it to a CSV file.

Iterates through every FTC team number and gathers the following attributes (for the specified season):

If a team played any matches in the specified season:
- team number
- team name
- team affiliation
- team location
- team rookie season
- wins
- losses
- ties
- matches played
- OPR
- NP OPR
- Highest qualifier points

Calculates the additional attributes of win percentage and parses location attributes

The attributes are then printed to a csv file.

Otherwise, it skips the team.

Since this script takes a long time to run, it sends and email when it is done.
"""

import time
import datetime
import alliancepy
from alliancepy import Season
import csv

startTime = time.time()

first_team = 1
last_team = 24000
act_teams = 0
inact_teams = 0
tot_teams = 0

client = alliancepy.Client(api_key="VpBih4206XpG8c+aDDFlBwhzd30tra5HYO14s+Qeyak="
, application_name="application_name")

for i in range (first_team, last_team): # range of team numbers to iterate through
    try:
        FTCteam = client.team(i)
        wins = FTCteam.season_wins(Season.SKYSTONE)
        losses = FTCteam.season_losses(Season.SKYSTONE)
        ties = FTCteam.season_ties(Season.SKYSTONE)
        matches_played = wins + losses + ties
        #print('Team ' + str(i))

        if (matches_played > 0):
            #print('active team')
            name = FTCteam.short_name
            affiliation = FTCteam.long_name
            location = FTCteam.location
            locs = location.split(',')
            city = locs[0].lstrip()
            state = locs[1].lstrip()
            country = locs[2].lstrip()
            zip = locs[3].lstrip()
            rookieyr = FTCteam.rookie_year
            last_active = FTCteam.last_active

            # gather season attributes
            #TODO: Try other seasons which are commented out in season.py (these need to be placed in the season.py file in the module in the alliancepy package)
            opr = FTCteam.opr(Season.SKYSTONE)
            npopr = FTCteam.np_opr(Season.SKYSTONE)
            # events = FTCteam.events(Season.SKYSTONE) - Need to work on this
            win_perc = wins / matches_played

            with open('act_team_stats.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    [i, name, affiliation, rookieyr, last_active, city, state, country, zip, wins, losses, ties, matches_played, win_perc, opr, npopr])

            act_teams += 1

        else:
            inact_teams += 1
            #print('inactive team')

    except:
        #print('no team')
        pass

tot_teams = act_teams + inact_teams
executionTime = (time.time() - startTime)
timestamp = datetime.datetime.now()

print(str(timestamp) + ' Execution time in seconds: ' + str(executionTime) + " total teams: " + str(tot_teams) + " active teams: " + str(act_teams) + " inactive teams: " + str(inact_teams))

#email a message when done.

