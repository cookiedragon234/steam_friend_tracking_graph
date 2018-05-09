import json, urllib2, sched, time, datetime, ast


#------------ SETTINGS - PLEASE FILL IN ------------#

# Your Steam API Key (Get one here: https://steamcommunity.com/dev/apikey)
# Example: "5SECIWKUZCXTCZOJ0KVGI7ZRWWK1CG2K"
key = ""
with open('apikey.txt', 'r') as thefile:
	key=str(thefile.read())

# Comma seperated list of steamids (This website can help you find someone's steam id: https://steamid.xyz/)
# Example: "81989695382653747,71392687122829707,53252835950609017,20886436082312703,22923101302782822"
ids = ""
with open('steamids.txt', 'r') as thefile:
	ids=str(thefile.read())

#------------ SETTINGS END ------------#


# Check that options have been filled in
if key == "" or ids == "":
	raise Exception('\nCONFIG NOT FILLED OUT!\n(Edit get.py)\n')

# Make an api request to steam
url1 = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
url = url1 + "?key=" + key + "&steamids=" + ids
response = urllib2.urlopen(url)

# Store and process the api request response
data = response.read()
data = data[12:]
data = data[:-1]
dict = json.loads(data)
list = json.dumps(dict['players'])
#list = ''.join(list)
list = list[1:]
list = list[:-1]
list = list.split("}, {")
final = ""

# Start sorting through data, delete whats useless and keep what isn't
peopleonline = 0
peopleplaying = 0
for x in list:
	#print "\n"
	#print x
	temp = str(x)
	if temp[-1:] != "}":
		temp = temp + "}"
	if temp[:1] != "{":
		temp = "{" + temp
	temp = json.loads(temp)

	# Don't actually need to delete, only count what's necessary so commented out
	'''
	if "steamid" in temp:
		del temp["steamid"]
	if "profileurl" in temp:
		del temp["profileurl"]
	if "realname" in temp:
		del temp["realname"]
	if "personastateflags" in temp:
		del temp["personastateflags"]
	if "communityvisibilitystate" in temp:
		del temp["communityvisibilitystate"]
	if "primaryclanid" in temp:
		del temp["primaryclanid"]
	if "timecreated" in temp:
		del temp["timecreated"]
	if "avatar" in temp:
		del temp["avatar"]
	if "commentpermission" in temp:
		del temp["commentpermission"]
	if "avatarfull" in temp:
		del temp["avatarfull"]
	if "avatarmedium" in temp:
		del temp["avatarmedium"]
	if "lastlogoff" in temp:
		del temp["lastlogoff"]
	if "loccountrycode" in temp:
		del temp["loccountrycode"]
	if "gameid" in temp:
		del temp["gameid"]
	if "profilestate" in temp:
		del temp["profilestate"]
	if "personaname" in temp:
		afg = temp['personaname']
		del temp['personaname']
		temp['name'] = afg
	if "personastate" in temp:
		afg = temp['personastate']
		del temp['personastate']
		temp['state'] = afg
	'''
	# What we're looking for, num of people playing and people online
	if "gameextrainfo" in temp:
		afg = temp['gameextrainfo']
		del temp['gameextrainfo']
		temp['game'] = afg
		peopleplaying = peopleplaying + 1
	if "personastate" in temp:
		#if temp["personastate"] == 0:
			#temp["personastate"] = "Offline"
		if temp["personastate"] == 1:
			#temp["personastate"] = "Online"
			peopleonline = peopleonline + 1
		if temp["personastate"] == 2:
			#temp["personastate"] = "Online"
			peopleonline = peopleonline + 1
		if temp["personastate"] == 3:
			#temp["personastate"] = "Online"
			peopleonline = peopleonline + 1
		if temp["personastate"] == 4:
			#temp["personastate"] = "Online"
			peopleonline = peopleonline + 1
		if temp["personastate"] == 5:
			#temp["personastate"] = "Online"
			peopleonline = peopleonline + 1
		if temp["personastate"] == 6:
			#temp["personastate"] = "Looking To Play"
			peopleonline = peopleonline + 1



# Join the people playing with the current unix time
newplayinglist = []
newplayinglist.append([int(time.time()), peopleplaying])

finalplayinglist = ''.join(str(e) for e in newplayinglist)
finalplayinglist = finalplayinglist + ",\n"


# Join the people online with the current unix time
newonlinelist = []
newonlinelist.append([int(time.time()), peopleonline])

finalonlinelist = ''.join(str(e) for e in newonlinelist)
finalonlinelist = finalonlinelist + ",\n"


#  ---- AMMENDABLE FILE ----  #

# People Playing
with open('playing_a.json', 'a') as thefile:
    thefile.write(finalplayinglist)

# People Online
with open('online_a.json', 'a') as thefile:
    thefile.write(finalonlinelist)


#  ---- READABLE FILE ----  #

# People Playing
with open('playing_a.json', 'r') as thefile:
	data=thefile.read().replace('\n', '')
data = data[:-1]
data = '{"people_playing":[' + data + "]}"

with open('playing_r.json', 'w') as thefile:
	thefile.write(data)

# People Online
with open('online_a.json', 'r') as thefile:
	data=thefile.read().replace('\n', '')
data = data[:-1]
data = '{"people_online":[' + data + "]}"

with open('online_r.json', 'w') as thefile:
	thefile.write(data)

# Cleanup data
# Online
with open('online_a.json', 'r') as thefile:
	data=thefile.read().replace('\n', '')
data = data[:-1]

last = ""
newdata = []
listlength = len(data)
for idx, x in enumerate(data):
    if idx == listlength -1:
        newdata.append(x)
    else:
        if data[idx][1] != data[idx-1][1] and data[idx][1] == data[idx+1][1]:
            newdata.append(x)
        if data[idx][1] != data[idx+1][1] and data[idx][1] == data[idx-1][1]:
            newdata.append(x)
        if data[idx][1] != data[idx+1][1] and data[idx][1] != data[idx-1][1]:
            newdata.append(x)
        last = x[1]
data = newdata

with open('online_a.json', 'w') as thefile:
	thefile.write(data)

data = '{"people_online":[' + data + "]}"
with open('online_r.json', 'w') as thefile:
	thefile.write(data)

# Playing
with open('playing_a.json', 'r') as thefile:
	data=thefile.read().replace('\n', '')
data = data[:-1]

last = ""
newdata = []
listlength = len(data)
for idx, x in enumerate(data):
    if idx == listlength -1:
        newdata.append(x)
    else:
        if data[idx][1] != data[idx-1][1] and data[idx][1] == data[idx+1][1]:
            newdata.append(x)
        if data[idx][1] != data[idx+1][1] and data[idx][1] == data[idx-1][1]:
            newdata.append(x)
        if data[idx][1] != data[idx+1][1] and data[idx][1] != data[idx-1][1]:
            newdata.append(x)
        last = x[1]
data = newdata

with open('playing_a.json', 'w') as thefile:
thefile.write(data)

data = '{"people_online":[' + data + "]}"
with open('playing_r.json', 'w') as thefile:
	thefile.write(data)
