"""
Script collects data from the Orange Alliance API and writes it to a CSV file.

Iterates through every FTC team number and gathers the following attributes (for the specified season):
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

Since this script takes a long time to run, it sends and email when it is done.
"""

import time
import datetime
import alliancepy
from alliancepy import Season
import csv

startTime = time.time()

tot_teams = 0
act_teams = 0
inact_teams = 0
reg_teams = 0
unreg_teams = 0
first_team = 1
last_team = 10000

client = alliancepy.Client(api_key="VpBih4206XpG8c+aDDFlBwhzd30tra5HYO14s+Qeyak="
, application_name="application_name")

for i in range (first_team, last_team): # range of team numbers to iterate through
    try:
        FTCteam = client.team(i)

        # gather team attributes
        name = FTCteam.short_name
        affiliation = FTCteam.long_name
        location = FTCteam.location
        locs = location.split(',')
        city = locs[0].lstrip()
        state = locs[1].lstrip()
        country = locs[2].lstrip()
        zip = locs[3].lstrip()
        #TODO: conditional here to fix leading zero on ZIP Codes
        #TODO: determine how to deal with no ZIP internationally.  May not matter much.
        rookieyr = FTCteam.rookie_year

        # gather season attributes
        #TODO: Try other seasons which are commented out in season.py (these need to be placed in the season.py file in the module in the alliancepy package)
        wins = FTCteam.season_wins(Season.SKYSTONE)
        losses = FTCteam.season_losses(Season.SKYSTONE)
        ties = FTCteam.season_ties(Season.SKYSTONE)
        matches_played = wins + losses + ties
        opr = FTCteam.opr(Season.SKYSTONE)
        npopr = FTCteam.np_opr(Season.SKYSTONE)
        # events = FTCteam.events(Season.SKYSTONE) - Need to work on this
        if (matches_played != 0):
            win_perc = wins / matches_played
            reg_teams = reg_teams + 1
        else:
            win_perc = -99
            inact_teams = inact_teams + 1
        #TODO: add highest_qualifier_score

        # print team attributes to csv file
        with open('team_stats.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([i, name, affiliation, rookieyr, city, state, country, zip, wins, losses, ties, matches_played, win_perc, opr, npopr])

        #print(str(i) + " " + name + " " + affiliation + " " + location + " " + str(wins) + " " + str(losses) + " " + str(ties) + " " + str(matches_played) + " " = str(win_perc) + " " + str(opr) + " " + str(npopr))

    except:

        with open('team_stats.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([i, -99, -99, -99, -99, -99, -99, -99, -99, -99, -99, -99])

        unreg_teams = unreg_teams + 1

#print("There is no team number: " + str(i))

tot_teams = reg_teams + unreg_teams + inact_teams
act_teams = tot_teams - (inact_teams + unreg_teams)
executionTime = (time.time() - startTime)
timestamp = datetime.datetime.now()

print(str(timestamp) + ' Execution time in seconds: ' + str(executionTime) + " total teams: " + str(tot_teams) + " active teams: " + str(act_teams) + " inactive teams: " + str(inact_teams) + " unregistered teams: " + str(unreg_teams))

with open('ftc_stats.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([str(timestamp) + " Execution time in seconds: " + str(executionTime) + " total teams: " + str(tot_teams) + " active teams: " + str(act_teams) + " inactive teams: " + str(inact_teams) + " unregistered teams: " + str(unreg_teams) + " First team: " + str(first_team) + " Last team: " + str(last_team)])

        #email a message when done.

