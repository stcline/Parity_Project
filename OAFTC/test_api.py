"""
Iterates through every FTC team number and gathers the following attributes (for the given season):
- team number
- team name
- team affiliation
- team location
- team wins
- team losses
- team ties
- team matches played
- team OPR
- team NP OPR

The attributes are then printed to a csv file.
"""

import alliancepy
from alliancepy import Season
import csv
client = alliancepy.Client(api_key="VpBih4206XpG8c+aDDFlBwhzd30tra5HYO14s+Qeyak="
, application_name="application_name")
#for i in range (1, 23102): #actual range of teams
for i in range (10000, 10500):#realistic test range
    try:
        FTCteam = client.team(i)

        # gather team attributes
        name = FTCteam.short_name
        affiliation = FTCteam.long_name
        location = FTCteam.location
        #TODO: conditional here to fix leading zero on ZIP Codes
        #TODO: parse location into city, state, country, ZIP. Remove 'location' attribute for these four. Eliminate empty quotes in csv.
        #TODO: determine how to deal with no ZIP internationally.  May not matter much.
        #rookie_year = FTCteam.rookie_year
        #TODO: understand this function to return the rookie year data

        # gather season attributes
        wins = FTCteam.season_wins(Season.SKYSTONE)
        losses = FTCteam.season_losses(Season.SKYSTONE)
        ties = FTCteam.season_ties(Season.SKYSTONE)
        matches_played = wins + losses + ties
        opr = FTCteam.opr(Season.SKYSTONE)
        npopr = FTCteam.np_opr(Season.SKYSTONE)
        if (matches_played != 0):
            win_perc = wins / matches_played
        else:
            win_perc = -99

# print team attributes to csv file
        with open('ftc_stats.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([i, name, affiliation, wins, losses, ties, matches_played, win_perc, opr, npopr])

        #print(str(i) + " " + name + " " + affiliation + " " + location + " " + str(wins) + " " + str(losses) + " " + str(ties) + " " + str(matches_played) + " " = str(win_perc) + " " + str(opr) + " " + str(npopr))

    except:

        with open('ftc_stats.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([i, -99, -99, -99, -99, -99, -99, -99, -99, -99, -99, -99])

        #print("There is no team number: " + str(i))

        #email a message when done.

