def printCondition():
	file = open("toppostsweather.txt", "r")
	sunny = "Sunny: "
	cloudy = "Cloudy: "
	rain = "Rain: "
	snow = "Snow: "
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		condition = parts1[1].split(": ")[1]
		if "Clear" in condition:
			sunny+=date+", "
		elif "Snow" in condition:
			snow+=date+", "
		elif "Cloud" in condition:
			cloudy+=date+", "
		else:
			rain+=date+", "

	print sunny[:-2]
	print cloudy[:-2]
	print rain[:-2]
	print snow[:-2]

	file.close()

def sunnyDates():
	file = open("toppostsweather.txt", "r")
	sunny = []
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		condition = parts1[1].split(": ")[1]
		if "Clear" in condition:
			sunny.append(date)

	file.close()
	return sunny

def rainyDates():
	file = open("toppostsweather.txt", "r")
	rain = []
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		condition = parts1[1].split(": ")[1]
		if "Rain" in condition or "Snow" in condition:
			rain.append(date)

	file.close()
	return rain

def cloudyDates():
	file = open("toppostsweather.txt", "r")
	cloudy = []
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		condition = parts1[1].split(": ")[1]
		if "Cloud" in condition or "Fog" in condition:
			cloudy.append(date)

	file.close()
	return cloudy

def snowyDates():
	file = open("toppostsweather.txt", "r")
	snow = []
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		condition = parts1[1].split(": ")[1]
		if "Snow" in condition:
			snow.append(date)

	file.close()
	return snow


def springDates():
	file = open("toppostsweather.txt", "r")
	spring = []
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		month = int(date[4:6])
		if month>=3 and month <=5:
			spring.append(date)

	file.close()
	return spring

def summerDates():
	file = open("toppostsweather.txt", "r")
	summer = []
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		month = int(date[4:6])
		if month>=6 and month <=8:
			summer.append(date)

	file.close()
	return summer

def fallDates():
	file = open("toppostsweather.txt", "r")
	fall = []
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		month = int(date[4:6])
		if month>=9 and month <=11:
			fall.append(date)

	file.close()
	return fall

def winterDates():
	file = open("toppostsweather.txt", "r")
	winter = []
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		month = int(date[4:6])
		if month==12 or month <=2:
			winter.append(date)

	file.close()
	return winter