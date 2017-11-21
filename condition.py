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
		if "Rain" in condition or "Overcast" in condition:
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
		if "Cloud" in condition:
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


