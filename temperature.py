def printTemperature():
	file = open("toppostsweather.txt", "r")
	cold = "Cold: "
	medium = "Mild: "
	hot = "Hot: "
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		temperature = parts1[2].split(": ")[1]
		if int(temperature)<40:
			cold+=date+", "
		elif int(temperature)>60:
			hot+=date+", "
		else:
			medium+=date+", "

	print cold[:-2]
	print medium[:-2]
	print hot[:-2]

	file.close()

def coldDates():
	file = open("toppostsweather.txt", "r")
	cold = []
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		temperature = parts1[2].split(": ")[1]
		if int(temperature)<40:
			cold.append(date)

	file.close()
	return cold

def mediumDates():
	file = open("toppostsweather.txt", "r")
	medium = []
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		temperature = parts1[2].split(": ")[1]
		if int(temperature)>=40 and int(temperature)<=60:
			medium.append(date)

	file.close()
	return medium

def hotDates():
	file = open("toppostsweather.txt", "r")
	hot = []
	for line in file:
		parts1 = line.split(",")
		date = parts1[0].split(": ")[1]
		temperature = parts1[2].split(": ")[1]
		if int(temperature)>60:
			hot.append(date)

	file.close()
	return hot