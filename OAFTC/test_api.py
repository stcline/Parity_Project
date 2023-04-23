import alliancepy
from alliancepy import Season

# SEASON = 'SKYSTONE'
season = ['XPOWERPLAY', 'XFREIGHT_FRENZY', 'XULTIMATE_GOAL', 'SKYSTONE', 'ROVER_RUCKUS', 'RELIC_RECOVERY', 'VELOCITY_VORTEX', 'XFIRST_RES-Q', 'XCASCADE_EFFECT', 'XBLOCK_PARTY!']
client = alliancepy.Client(api_key="VpBih4206XpG8c+aDDFlBwhzd30tra5HYO14s+Qeyak="
, application_name="application_name")
for i in range (5115, 5125):
	try:
		team = client.team(i)
		val = team.season_wins(Season.Freight_Frenzy)
		print("team: " + str(i) + " val: " + str(val))
	except:
		print("There is no team number: " + str(i))
