import json, urllib2, sched, time, datetime, ast


#------------ SETTINGS - PLEASE FILL IN ------------#

# Your Steam API Key (Get one here: https://steamcommunity.com/dev/apikey)
# Example: "5SECIWKUZCXTCZOJ0KVGI7ZRWWK1CG2K"
url2 = "FCD9837C175734430FEEE03B5814F963"

#Comma seperated list of steamids (This website can help you find someone's steam id: https://steamid.xyz/)
# Example: "81989695382653747,71392687122829707,53252835950609017,20886436082312703,22923101302782822"
url3 = "76561198053057263,76561198218944852,76561197971991612,76561198011645574,76561198327822088,76561198354786065,76561198148033507,76561198316763129,76561198253314526,76561198175682481,76561198117505847,76561198055461483,76561198342538785,76561198148033507,76561198026258791,76561198080613430"

#------------ SETTINGS END ------------#


url1 = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"

url = url1 + "?key=" + url2 + "&steamids=" + url3

response = urllib2.urlopen(url)
data = response.read()
data = data[12:]
data = data[:-1]
#print data
dict = json.loads(data)
#print dict['players']
list = json.dumps(dict['players'])
#list = ''.join(list)
list = list[1:]
list = list[:-1]
list = list.split("}, {")
#print "\n\nList"
#print list
final = ""


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
	if "steamid" in temp:
		del temp["steamid"]
	if "profileurl" in temp:
		del temp["profileurl"]
	if "realname" in temp:
		del temp["realname"]
	if "personastate" in temp:
		if temp["personastate"] == 0:
			temp["personastate"] = "Offline"
		if temp["personastate"] == 1:
			temp["personastate"] = "Online"
		if temp["personastate"] == 2:
			temp["personastate"] = "Online"
		if temp["personastate"] == 3:
			temp["personastate"] = "Online"
		if temp["personastate"] == 4:
			temp["personastate"] = "Online"
		if temp["personastate"] == 5:
			temp["personastate"] = "Online"
		if temp["personastate"] == 6:
			temp["personastate"] = "Looking To Play"
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
	if "gameextrainfo" in temp:
		afg = temp['gameextrainfo']
		del temp['gameextrainfo']
		temp['game'] = afg
		peopleplaying = peopleplaying + 1
	
theactuallist = []
okcount = peopleplaying
theactuallist.append([int(time.time()), peopleplaying])
print theactuallist

okthislistpls = ''.join(str(e) for e in theactuallist)
okthislistpls = okthislistpls + ",\n"



#AMMENDABLE FILE
thefile = open('readdata.json', 'a')
thefile.write(okthislistpls)
thefile.close()

print okthislistpls


#MAKE READABLE FILE
with open('readdata.json', 'r') as myfile:
    data=myfile.read().replace('\n', '')
data = data[:-1]
data = '{"people_playing":[' + data + "]}"

thefile = open('data.json', 'w')
thefile.write(data)
thefile.close()
